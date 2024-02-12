from django.contrib.gis.geos import MultiPolygon, Polygon
from django.test import TestCase, Client
from django.urls import reverse
from ..models import VideoShapefile, GADMShapefile, GADMCountries, GADMProvinces


# Simple square polygon to use in geospatial data table tests
square = MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))

class ModelTest(TestCase):
    def test_video_shapefile_creation(self):
        video_shapefile = VideoShapefile.objects.create(
            geom=square,
            name="Test shape",
            polity="Test polity",
            seshat_id="Test seshat_id",
            area=100.0,
            start_year=2000,
            end_year=2020,
            polity_start_year=2000,
            polity_end_year=2020,
            colour="#FFFFFF"
        )
        self.assertIsInstance(video_shapefile, VideoShapefile)
        self.assertEqual(video_shapefile.name, "Test shape")

    def test_gadm_shapefile_creation(self):
        gadm_shapefile = GADMShapefile.objects.create(
            geom=square,
            UID=123456789,
            NAME_0="Test shape"
        )
        self.assertIsInstance(gadm_shapefile, GADMShapefile)
        self.assertEqual(gadm_shapefile.NAME_0, "Test shape")

    def test_gadm_countries_creation(self):
        gadm_countries = GADMCountries.objects.create(
            geom=square,
            COUNTRY="Test Country"
        )
        self.assertIsInstance(gadm_countries, GADMCountries)
        self.assertEqual(gadm_countries.COUNTRY, "Test Country")

    def test_gadm_provinces_creation(self):
        gadm_provinces = GADMProvinces.objects.create(
            geom=square,
            NAME_1="Test Province"
        )
        self.assertIsInstance(gadm_provinces, GADMProvinces)
        self.assertEqual(gadm_provinces.NAME_1, "Test Province")

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_map_view_initial(self):
        response = self.client.get(reverse('core/world_map/'))
        self.assertEqual(response.status_code, 200)

    def test_map_view_all(self):
        response = self.client.get(reverse('core/world_map_all/'))
        self.assertEqual(response.status_code, 200)

    def test_provinces_and_countries_view(self):
        response = self.client.get(reverse('core/provinces_and_countries'))
        self.assertEqual(response.status_code, 200)