from django.contrib.gis.gdal import DataSource
from django.core.management.base import BaseCommand
from seshat.apps.core.models import GADMShapefile

class Command(BaseCommand):
    help = 'Populates the GADMShapefile table with features from a GeoPackage'

    def add_arguments(self, parser):
        parser.add_argument('gpkg_file', type=str, help='Path to the GeoPackage file')

    def handle(self, *args, **options):
        gpkg_file = options['gpkg_file']

        data_source = DataSource(gpkg_file)
        layer = data_source[0]  # Access the first layer in the GeoPackage

        for feature in layer:
            geom = feature.geom  # Retrieve the geometry of the feature
            # Creating a GEOSGeometry object from the feature's geometry
            geom_gis = geom.geos

            # Additional fields can be obtained based on the fields available in the layer
            name = feature.get('name_1')

            # Create an entry in the GADMShapefile model for each feature in the layer
            GADMShapefile.objects.create(
                geom=geom_gis,
                name=name,  # Include other fields here as required
                # Add other fields based on the data available in the GeoPackage
                # TODO: update this
            )

            self.stdout.write(self.style.SUCCESS(f"Inserted feature into the GADMShapefile table."))
