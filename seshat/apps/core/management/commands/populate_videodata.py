import os
import json
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from seshat.apps.core.models import VideoShapefile

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

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
                    geom=GEOSGeometry(json.dumps(feature['geometry']))
                    # Convert Polygon to MultiPolygon if necessary
                    if geom.geom_type == 'Polygon':
                        geom = MultiPolygon(geom)

                    if properties['Type'] == 'POLITY':
                        VideoShapefile.objects.create(
                            geom=geom,
                            name=properties['Name'],
                            name_underscores=properties['PolID'],
                            wikipedia_name=properties['Wikipedia'],
                            seshat_id=properties['SeshatID'],
                            area=properties['Area_km2'],
                            start_year=properties['Year'],
                            end_year=properties['Year']  # TODO: Adjust as needed
                        )

                self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {filename}'))
