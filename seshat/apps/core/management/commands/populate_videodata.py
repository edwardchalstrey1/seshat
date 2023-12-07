import os
import geopandas as gpd
from django.core.management.base import BaseCommand
from seshat.apps.core.models import VideoShapefile
from shapely.geometry import shape

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        for filename in os.listdir(dir):
            if filename.endswith('.geojson'):
                filepath = os.path.join(dir, filename)

                # Load GeoJSON file using geopandas
                gdf = gpd.read_file(filepath)

                for index, row in gdf.iterrows():
                    # Extract fields from GeoDataFrame and create VideoShapefile object
                    video_shapefile = VideoShapefile(
                        geom=shape(row.geometry),
                        name=row['Name'],
                        name_underscores=row['PolID'],
                        start_year=row['Year'],
                        area=row['Area_km2'],
                        seshat_id=row['SeshatID'],
                        wikipedia_name=row['Wikipedia'],
                    )
                    video_shapefile.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully loaded data from {filename}'))
