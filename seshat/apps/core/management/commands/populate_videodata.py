import os
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from seshat.apps.core.models import VideoShapefile
import geopandas as gpd

class Command(BaseCommand):
    """
    Iterate through geojson files in the provided directory.
    Populate the core_videoshapefile table with the geojson fields.
    """
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        # Iterate through each file in the base directory
        for file_name in os.listdir(dir):
            if file_name.endswith(".geojson"):
                file_path = os.path.join(dir, file_name)

                # Read GeoJSON file using geopandas
                gdf = gpd.read_file(file_path)

                # Iterate through features and populate VideoShapefile model
                for _, row in gdf.iterrows():
                    geom = GEOSGeometry(row.geometry)
                    name = row.Name
                    name_underscores = row.PolID
                    start_year = row.Year
                    area = row.Area_km2
                    seshat_id = row.SeshatID
                    wikipedia_name = row.Wikipedia

                    # Create VideoShapefile instance and save to the database
                    VideoShapefile.objects.create(
                        geom=geom,
                        name=name,
                        name_underscores=name_underscores,
                        start_year=start_year,
                        area=area,
                        seshat_id=seshat_id,
                        wikipedia_name=wikipedia_name
                    )

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {file_name}'))
