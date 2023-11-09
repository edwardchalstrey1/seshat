import os
import csv
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from seshat.apps.core.models import MacrostateShapefile

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

                # Load the geometry using DataSource from the shapefile
                data_source = DataSource(shp_file)
                layer = data_source[0]

                print(layer.fields)

                print(layer.geom_type)

                print(layer.srs)


