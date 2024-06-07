import unittest
from practice11_1 import get_formatted_city_country

class CityCountryTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_name = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
