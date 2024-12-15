import unittest
from test_Restaurant_Browsing import RestaurantBrowsing, RestaurantDatabase

class TestRestaurantBrowsingWhiteBox(unittest.TestCase):
    def test_search_by_filters(self):
        database = RestaurantDatabase()
        browsing = RestaurantBrowsing(database)
        results = browsing.search_by_filters(cuisine_type="Italian", location="Downtown", min_rating=4.0)
        self.assertEqual(len(results), 1)

    def test_get_restaurants(self):
        database = RestaurantDatabase()
        restaurants = database.get_restaurants()
        self.assertEqual(len(restaurants), 5)

if __name__ == '__main__':
    unittest.main()