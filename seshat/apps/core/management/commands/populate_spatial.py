import os
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand
from seshat.apps.core.models import MacrostateShapefile

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('base_dir', type=str, help='Base directory containing shapefiles')

    def handle(self, *args, **options):
        base_dir = options['base_dir']

        for dirpath, dirnames, filenames in os.walk(base_dir):
            for file in filenames:
                if file.endswith(".shp"):
                    shp_file = os.path.join(dirpath, file)
                    shape_name = os.path.splitext(file)[0]

                    data_source = DataSource(shp_file)
                    layer = data_source[0]
                    geom = GEOSGeometry(layer[0].geom.wkt)
                    instance = MacrostateShapefile.objects.create(geom=geom, name=shape_name)

                    self.stdout.write(self.style.SUCCESS(f"Inserted '{shape_name}' from '{shp_file}' into the database."))
