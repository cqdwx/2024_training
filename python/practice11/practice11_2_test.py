import unittest
from practice11_2 import get_formatted_city_country

class CityCountryTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_name = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')
    
    def test_city_country_population(self):
        formatted_name = get_formatted_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
