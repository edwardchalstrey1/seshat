import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from django.core.management.base import BaseCommand
from seshat.apps.core.models import GADMShapefile

class Command(BaseCommand):
    """
    Iterate through the provided directory.
    Find shapefiles in the subdirs.
    Populate the core_gadmshapefile table with the shape's MultiPolygon and filename.
    """
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('base_dir', type=str, help='Base directory containing shapefiles')

    def handle(self, *args, **options):
        base_dir = options['base_dir']

        for filename in os.listdir(base_dir):
            if filename.endswith(".shp"):
                shp_file = os.path.join(base_dir, filename)
                ds = DataSource(shp_file)
                layer = ds[0]
                print(layer.fields)
                print(len(layer))
                print(layer.geom_type)
                print(layer.srs)
                # break

                
                # mapping = {
                #     "name": "str",
                #     "poly": "POLYGON",
                # }
                # lm = LayerMapping(GADMShapefile, shp_file, mapping)
                # lm.save(verbose=True)  # Save the layermap, imports the data.

