import os
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Polygon
from django.core.management.base import BaseCommand
from seshat.apps.core.models import MacrostateShapefile

class Command(BaseCommand):
    """
        Iterate through the provided directory.
        Find shapefiles in the subdirs.
        Populate the core_macrostateshapefile table with the shape's MultiPolygon and filename.
    """
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

                    # Load the geometry using DataSource from the shapefile
                    data_source = DataSource(shp_file)
                    layer = data_source[0]

                    # Get the first feature in the layer
                    feature = layer[0]

                    # Convert the geometry to a GEOSGeometry object
                    geom = GEOSGeometry(feature.geom.wkt)

                    # Convert Polygon to MultiPolygon if necessary
                    if geom.geom_type == 'Polygon':
                        geom = MultiPolygon(geom)

                    # Save the table row
                    instance = MacrostateShapefile.objects.create(geom=geom, name=shape_name)

                    # Print completion to terminal
                    self.stdout.write(self.style.SUCCESS(f"Inserted '{shape_name}' from '{shp_file}' into the database."))
