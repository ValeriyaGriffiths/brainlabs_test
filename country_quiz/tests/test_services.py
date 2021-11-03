import unittest
from ..services import get_country_data_from_external_api


class TestStringMethods(unittest.TestCase):

    def test_expected_country_data_keys(self):
        data = get_country_data_from_external_api()
        self.assertTrue('name' in data and 'capital' in data)

    def test_returned_countries_are_reasonably_random(self):
        countries = [get_country_data_from_external_api() for _ in range(3)]
        self.assertFalse(all(c == countries[0] for c in countries))
