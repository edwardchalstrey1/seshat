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

        # Mapping to store the maximum end_year for each file_name
        max_end_years = {}

        # Iterate over files in the directory
        for filename in os.listdir(dir):
            if filename.endswith('.geojson'):
                file_path = os.path.join(dir, filename)

                # Extract file_name and end_year from the filename
                parts = os.path.splitext(filename)[0].split('_')
                file_name = '_'.join(parts[:-1])
                end_year_str = parts[-1]

                # Convert end_year to an integer
                if 'BCE' in end_year_str:
                    end_year = int(end_year_str.replace('BCE', '')) * -1
                elif 'CE' in end_year_str:
                    end_year = int(end_year_str.replace('CE', ''))

                # Read and parse the GeoJSON file
                with open(file_path, 'r') as geojson_file:
                    geojson_data = json.load(geojson_file)

                # Extract data and create VideoShapefile instances
                for feature in geojson_data['features']:
                    properties = feature['properties']
                    geom = GEOSGeometry(json.dumps(feature['geometry']))

                    # Convert Polygon to MultiPolygon if necessary
                    if geom.geom_type == 'Polygon':
                        geom = MultiPolygon(geom)

                    if properties['Type'] == 'POLITY':
                        # Update max_end_years for the current file_name
                        max_end_years[file_name] = max(max_end_years.get(file_name, float('-inf')), end_year)

                        VideoShapefile.objects.create(
                            geom=geom,
                            name=properties['Name'],
                            name_underscores=properties['PolID'],
                            wikipedia_name=properties['Wikipedia'],
                            seshat_id=properties['SeshatID'],
                            area=properties['Area_km2'],
                            start_year=properties['Year'],
                            end_year=max_end_years[file_name]  # Use the determined end_year
                        )

                self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {filename}'))
