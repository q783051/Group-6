import unittest
from test_Restaurant_Browsing import RestaurantBrowsing, RestaurantDatabase

class TestRestaurantBrowsingBlackBox(unittest.TestCase):
    def test_search_by_cuisine(self):
        database = RestaurantDatabase()
        browsing = RestaurantBrowsing(database)
        results = browsing.search_by_cuisine("Italian")
        self.assertEqual(len(results), 2)

    def test_search_by_location(self):
        database = RestaurantDatabase()
        browsing = RestaurantBrowsing(database)
        results = browsing.search_by_location("Downtown")
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()