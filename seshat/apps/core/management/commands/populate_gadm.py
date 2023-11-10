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

            # Create an entry in the GADMShapefile model for each feature in the layer
            GADMShapefile.objects.create(
                geom=geom_gis,
                UID=feature.get('UID'),
                GID_0=feature.get('GID_0'),
                NAME_0=feature.get('NAME_0'),
                VARNAME_0=feature.get('VARNAME_0'),
                GID_1=feature.get('GID_1'),
                NAME_1=feature.get('NAME_1'),
                VARNAME_1=feature.get('VARNAME_1'),
                NL_NAME_1=feature.get('NL_NAME_1'),
                ISO_1=feature.get('ISO_1'),
                HASC_1=feature.get('HASC_1'),
                CC_1=feature.get('CC_1'),
                TYPE_1=feature.get('TYPE_1'),
                ENGTYPE_1=feature.get('ENGTYPE_1'),
                VALIDFR_1=feature.get('VALIDFR_1'),
                GID_2=feature.get('GID_2'),
                NAME_2=feature.get('NAME_2'),
                VARNAME_2=feature.get('VARNAME_2'),
                NL_NAME_2=feature.get('NL_NAME_2'),
                HASC_2=feature.get('HASC_2'),
                CC_2=feature.get('CC_2'),
                TYPE_2=feature.get('TYPE_2'),
                ENGTYPE_2=feature.get('ENGTYPE_2'),
                VALIDFR_2=feature.get('VALIDFR_2'),
                GID_3=feature.get('GID_3'),
                NAME_3=feature.get('NAME_3'),
                VARNAME_3=feature.get('VARNAME_3'),
                NL_NAME_3=feature.get('NL_NAME_3'),
                HASC_3=feature.get('HASC_3'),
                CC_3=feature.get('CC_3'),
                TYPE_3=feature.get('TYPE_3'),
                ENGTYPE_3=feature.get('ENGTYPE_3'),
                VALIDFR_3=feature.get('VALIDFR_3'),
                GID_4=feature.get('GID_4'),
                NAME_4=feature.get('NAME_4'),
                VARNAME_4=feature.get('VARNAME_4'),
                CC_4=feature.get('CC_4'),
                TYPE_4=feature.get('TYPE_4'),
                ENGTYPE_4=feature.get('ENGTYPE_4'),
                VALIDFR_4=feature.get('VALIDFR_4'),
                GID_5=feature.get('GID_5'),
                NAME_5=feature.get('NAME_5'),
                CC_5=feature.get('CC_5'),
                TYPE_5=feature.get('TYPE_5'),
                ENGTYPE_5=feature.get('ENGTYPE_5'),
                GOVERNEDBY=feature.get('GOVERNEDBY'),
                SOVEREIGN=feature.get('SOVEREIGN'),
                DISPUTEDBY=feature.get('DISPUTEDBY'),
                REGION=feature.get('REGION'),
                VARREGION=feature.get('VARREGION'),
                COUNTRY=feature.get('COUNTRY'),
                CONTINENT=feature.get('CONTINENT'),
                SUBCONT=feature.get('SUBCONT')
            )

            self.stdout.write(self.style.SUCCESS(f"Inserted feature into the GADMShapefile table."))
