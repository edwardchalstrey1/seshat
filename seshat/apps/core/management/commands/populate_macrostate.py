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
    Populate the core_macrostateshapefile table with the shape's MultiPolygon and filename.
    """
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('base_dir', type=str, help='Base directory containing shapefiles')

    def handle(self, *args, **options):
        base_dir = options['base_dir']

        # Read the CSV file
        csv_path = os.path.join(base_dir, 'macrostate_data.csv')
        csv_data = {}
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter='|')
            for row in csv_reader:
                value_from = row['Value.From']
                csv_data[value_from] = {
                    'polity': row['Polity'],
                    'date_from': row['Date.From'],
                    'date_to': row['Date.To']
                }

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

                    # Save the table row with associated CSV data
                    instance = MacrostateShapefile.objects.create(
                        geom=geom,
                        name=shape_name,
                        polity=csv_data.get(shape_name, {}).get('polity'),
                        date_from=csv_data.get(shape_name, {}).get('date_from'),
                        date_to=csv_data.get(shape_name, {}).get('date_to')
                    )

                    # Print completion to terminal
                    self.stdout.write(self.style.SUCCESS(f"Inserted '{shape_name}' from '{shp_file}' into the database."))
