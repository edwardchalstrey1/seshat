import os
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from seshat.apps.core.models import VideoShapefile

class Command(BaseCommand):
    """
    Iterate through geojson files in the provided directory.
    Populate the core_videoshapefile table with the geojson fields.
    """
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('base_dir', type=str, help='Base directory containing geojson files')

    def handle(self, *args, **options):
        base_dir = options['base_dir']