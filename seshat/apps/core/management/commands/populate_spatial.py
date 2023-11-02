import os
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
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

                    # Assuming the shape_name is unique and identifies the same row as the geom
                    instance = MacrostateShapefile.objects.create(
                        geom=GEOSGeometry(shp_file),
                    )
                    
                    # Set the name field using the shape_name
                    instance.name = shape_name
                    instance.save()