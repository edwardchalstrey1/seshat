import os
from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
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

                    mapping = {
                        'geom': 'MULTIPOLYGON',
                    }

                    lm = LayerMapping(
                        MacrostateShapefile, shp_file, mapping,
                        transform=False, encoding='utf-8',
                    )
                    lm.save(strict=True, verbose=True)

                    self.stdout.write(self.style.SUCCESS(f"Inserted '{shape_name}' from '{shp_file}' into the database."))
