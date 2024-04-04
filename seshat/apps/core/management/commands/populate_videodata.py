import os
import json
from distinctipy import get_colors, get_hex
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from django.db import connection
from seshat.apps.core.models import VideoShapefile, Polity
from seshat.apps.general.models import POLITY_LANGUAGE_CHOICES, Polity_language

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        # Clear the VideoShapefile table
        self.stdout.write(self.style.SUCCESS('Deleting all existing VideoShapefile data'))
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

                        try:
                            polity_id = properties['PolID']
                        except KeyError:
                            polity_id = properties['Name'].replace(' ', '_')

                        # Save the years so we can determine the end year
                        if polity_id not in polity_years:
                            polity_years[polity_id] = []
                        polity_years[polity_id].append(properties['Year'])

                        all_polities.add(polity_id)

                        self.stdout.write(self.style.SUCCESS(f'Found shape for {properties["Name"]} ({properties["Year"]})'))

        # Sort the polities and generate a colour mapping
        unique_polities = sorted(all_polities)
        self.stdout.write(self.style.SUCCESS(f'Generating colour mapping for {len(unique_polities)} polities'))
        pol_col_map = colour_mapping(unique_polities)
        self.stdout.write(self.style.SUCCESS(f'Colour mapping generated'))

        # Sort the languages and generate a colour mapping
        self.stdout.write(self.style.SUCCESS(f'Generating colour mapping for {len(POLITY_LANGUAGE_CHOICES)} languages'))
        lang_col_map = colour_mapping([x[0] for x in POLITY_LANGUAGE_CHOICES])
        self.stdout.write(self.style.SUCCESS(f'Colour mapping generated'))

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

                        try:
                            polity_id = properties['PolID']
                        except KeyError:
                            polity_id = properties['Name'].replace(' ', '_')

                        self.stdout.write(self.style.SUCCESS(f'Importing shape for {properties["Name"]} ({properties["Year"]})'))
                        
                        # Get a sorted list of the shape years this polity
                        this_polity_years = sorted(polity_years[polity_id])

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

                        # Determine the language and colour of the polity shape
                        language = 'Uncoded'
                        language_colour = 'grey'
                        if properties['SeshatID'] != 'none':
                            try:
                                polity = Polity.objects.get(new_name=properties['SeshatID'])
                                try:
                                    polity_language = Polity_language.objects.filter(polity_id=polity.id).first()  # TODO: update to get all languages
                                    language = polity_language.language
                                    language_colour = lang_col_map[language]
                                except:
                                    pass
                            except Polity.DoesNotExist:  # TODO: remove this when there are no longer seshat_id's in the Cliopatria data that don't exist in the Polity table
                                pass

                        VideoShapefile.objects.create(
                            geom=geom,
                            name=properties['Name'],
                            polity=polity_id,
                            wikipedia_name=properties['Wikipedia'],
                            seshat_id=properties['SeshatID'],
                            area=properties['Area_km2'],
                            start_year=properties['Year'],
                            end_year=end_year,
                            polity_start_year=polity_start_year,
                            polity_end_year=polity_end_year,
                            colour=pol_col_map[polity_id],
                            language=language,
                            language_colour=language_colour
                        )

                        self.stdout.write(self.style.SUCCESS(f'Successfully imported shape for {properties["Name"]} ({properties["Year"]})'))

                self.stdout.write(self.style.SUCCESS(f'Successfully imported all data from {filename}'))

        self.stdout.write(self.style.SUCCESS('Adding simplified geometries for faster loading...'))
        # Adjust the tolerance param of ST_Simplify as needed
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE core_videoshapefile 
                SET simplified_geom = ST_Simplify(geom, 0.07);
            """)
        self.stdout.write(self.style.SUCCESS('Simplified geometries added'))
        


def colour_mapping(entities):
    """Use DistinctiPy package to assign a colour to each entity in a list of entities."""
    colours = []
    for col in get_colors(len(entities)):
        colours.append(get_hex(col))
    return dict(zip(entities, colours))
