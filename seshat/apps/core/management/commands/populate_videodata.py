import os
import json
from datetime import datetime
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from seshat.apps.core.models import VideoShapefile

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        # Dict of all the shape years for a given polity
        polity_years = {}
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

                        # Get the end year for a shape from the next shape for that polity start year minus one
                        this_polity_years =  sorted(polity_years[properties['PolID']])
                        this_year_index = this_polity_years.index(properties['Year'])
                        try:
                            end_year = this_polity_years[this_year_index+1] - 1
                        except:
                            end_year = datetime.now().year # Assume the last shape runs until present day TODO: change this to the polity end date later
                        
                        # Save geom and convert Polygon to MultiPolygon if necessary
                        geom=GEOSGeometry(json.dumps(feature['geometry']))
                        if geom.geom_type == 'Polygon':
                            geom = MultiPolygon(geom)

                        VideoShapefile.objects.create(
                            geom=geom,
                            name=properties['Name'],
                            name_underscores=properties['PolID'],
                            wikipedia_name=properties['Wikipedia'],
                            seshat_id=properties['SeshatID'],
                            area=properties['Area_km2'],
                            start_year=properties['Year'],
                            end_year=end_year
                        )

                self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {filename}'))
