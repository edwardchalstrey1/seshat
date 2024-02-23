import os
import json
from distinctipy import get_colors, get_hex
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from seshat.apps.core.models import VideoShapefile

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        # Clear the VideoShapefile table
        VideoShapefile.objects.all().delete()

        # Get the start and end years for each shape
        # Load a file called name_years.json kept in the same dir as the geojson files.
        # Loads a dict of polity names and their start and end years.
        # The values are lists of the form [[first_start_year, first_end_year], [second_start_year, second_end_year], ...]
        name_years_path = os.path.join(dir, 'name_years.json')
        with open(name_years_path, 'r') as f:
            name_years = json.load(f)

        # Dict of all the shape years for a given polity
        polity_years = {}
        # Set of all polities, for generating colour mapping
        all_polities = set()
        # Iterate over files in the directory
        for filename in os.listdir(dir):
            if filename.endswith('.geojson'):
                file_path = os.path.join(dir, filename)

                # Read and parse the GeoJSON file
                with open(file_path, 'r') as geojson_file:
                    geojson_data = json.load(geojson_file)

                # Extract data and create VideoShapefile instances
                for feature in geojson_data['features']:
                    properties = feature['properties']
                    if properties['Type'] == 'POLITY':

                        # Save the years so we can determine the end year
                        if properties['PolID'] not in polity_years:
                            polity_years[properties['PolID']] = []
                        polity_years[properties['PolID']].append(properties['Year'])

                        all_polities.add(properties['PolID'])

                self.stdout.write(self.style.SUCCESS(f'Successfully extracted date for {filename}'))
        unique_polities = sorted(all_polities)
        pol_col_map = polity_colour_mapping(unique_polities)

        # Iterate over files in the directory
        for filename in os.listdir(dir):
            if filename.endswith('.geojson'):
                file_path = os.path.join(dir, filename)

                # Read and parse the GeoJSON file
                with open(file_path, 'r') as geojson_file:
                    geojson_data = json.load(geojson_file)

                # Extract data and create VideoShapefile instances
                for feature in geojson_data['features']:
                    properties = feature['properties']
                    if properties['Type'] == 'POLITY':
                        
                        # Get a sorted list of the shape years this polity
                        this_polity_years = sorted(polity_years[properties['PolID']])

                        # Get the polity start and end years
                        polity_start_year = this_polity_years[0]
                        polity_end_year = this_polity_years[-1]

                        # Get the end year for a shape    
                        # Most of the time, the shape end year is the year of the next shape
                        # Some polities have a gap in their active years
                        # For a shape year at the start of a gap, set the end year to be the shape year, so it doesn't cover the inactive period
                        start_end_years = name_years[properties['Name']]
                        end_years = [x[1] for x in start_end_years]
                        if properties['Year'] in end_years:
                            end_year = properties['Year']
                        else:
                            this_year_index = this_polity_years.index(properties['Year'])
                            try:
                                end_year = this_polity_years[this_year_index + 1] - 1
                            except IndexError:
                                end_year = polity_end_year
                        
                        # Save geom and convert Polygon to MultiPolygon if necessary
                        geom = GEOSGeometry(json.dumps(feature['geometry']))
                        if geom.geom_type == 'Polygon':
                            geom = MultiPolygon(geom)

                        VideoShapefile.objects.create(
                            geom=geom,
                            name=properties['Name'],
                            polity=properties['PolID'],
                            wikipedia_name=properties['Wikipedia'],
                            seshat_id=properties['SeshatID'],
                            area=properties['Area_km2'],
                            start_year=properties['Year'],
                            end_year=end_year,
                            polity_start_year=polity_start_year,
                            polity_end_year=polity_end_year,
                            colour=pol_col_map[properties['PolID']]
                        )

                self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {filename}'))


def polity_colour_mapping(polities):
    """Use DistinctiPy package to assign a colour to each polity"""
    colours = []
    for col in get_colors(len(polities)):
        colours.append(get_hex(col))
    return dict(zip(polities, colours))
