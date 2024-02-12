from django.contrib.gis.geos import MultiPolygon, Polygon
from django.test import TestCase, Client
from django.urls import reverse
from ..models import VideoShapefile, GADMShapefile, GADMCountries, GADMProvinces, Polity
from ..views import get_polity_year_range, get_provinces, get_polity_shapes, get_polity_info, get_polity_shape_content, get_all_polity_capitals
from ..templatetags.core_tags import get_polity_capitals, polity_map


# Simple square polygon to use in geospatial data table tests
square = MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))

class ShapesTest(TestCase):
    """Test case for the shape models and views."""

    def setUp(self):
        """Set up the test client and Polity entry for the view functions."""
        self.client = Client()
        self.polity = Polity.objects.create(name='TestPolity', id=1, long_name='TestPolity', new_name='TestPolity')
        self.video_shapefile = VideoShapefile.objects.create(
            geom=square,
            name="Test shape",
            polity="Testpolity",
            seshat_id="Test seshat_id",
            area=100.0,
            start_year=2000,
            end_year=2020,
            polity_start_year=2000,
            polity_end_year=2020,
            colour="#FFFFFF"
        )

    # Model tests

    def test_video_shapefile_creation(self):
        """Test the creation of a VideoShapefile instance."""
        self.assertIsInstance(self.video_shapefile, VideoShapefile)
        self.assertEqual(self.video_shapefile.name, "Test shape")

    def test_gadm_shapefile_creation(self):
        """Test the creation of a GADMShapefile instance."""
        gadm_shapefile = GADMShapefile.objects.create(
            geom=square,
            UID=123456789,
            NAME_0="Test shape"
        )
        self.assertIsInstance(gadm_shapefile, GADMShapefile)
        self.assertEqual(gadm_shapefile.NAME_0, "Test shape")

    def test_gadm_countries_creation(self):
        """Test the creation of a GADMCountries instance."""
        gadm_countries = GADMCountries.objects.create(
            geom=square,
            COUNTRY="Test Country"
        )
        self.assertIsInstance(gadm_countries, GADMCountries)
        self.assertEqual(gadm_countries.COUNTRY, "Test Country")

    def test_gadm_provinces_creation(self):
        """Test the creation of a GADMProvinces instance."""
        gadm_provinces = GADMProvinces.objects.create(
            geom=square,
            NAME_1="Test Province"
        )
        self.assertIsInstance(gadm_provinces, GADMProvinces)
        self.assertEqual(gadm_provinces.NAME_1, "Test Province")

    # View function tests

    def test_get_polity_year_range(self):
        """Test the get_polity_year_range function."""
        seshat_id = 'TestPolity'
        expected_result = (2000, 2020)
        result = get_polity_year_range(seshat_id)
        self.assertEqual(result, expected_result)

    def test_get_polity_info(self):
        """Test the get_polity_info function."""
        seshat_ids = ['TestPolity']
        expected_result = [('TestPolity', 1, 'TestPolity')]
        result = get_polity_info(seshat_ids)
        self.assertEqual(result, expected_result)

    # def test_get_polity_shape_content(self):
    #     """Test the get_polity_shape_content function."""
    #     result = get_polity_shape_content()
    #     expected_result = {
    #         'shapes': [{'seshat_id': 'TestPolity', 'start_year': 2000, 'end_year': 2020, 'geom': square}],
    #         'earliest_year': 2000,
    #         'display_year': 2000,
    #         'latest_year': 2020,
    #         'seshat_id_page_id': {'TestPolity': {'id': 1, 'long_name': 'TestPolity'}}
    #     }
    #     self.assertEqual(result, expected_result)

    # def test_map_view_initial(self):
    #     """Test the initial map view."""
    #     response = self.client.get(reverse('world_map'))
    #     self.assertEqual(response.status_code, 200)

    # def test_map_view_all(self):
    #     """Test the map view with all data."""
    #     response = self.client.get(reverse('world_map_all'))
    #     self.assertEqual(response.status_code, 200)

    # def test_provinces_and_countries_view(self):
    #     """Test the provinces and countries view."""
    #     response = self.client.get(reverse('provinces_and_countries'))
    #     self.assertEqual(response.status_code, 200)