import unittest
from test_Order_Placement import Cart, OrderPlacement, UserProfile, RestaurantMenu

class TestOrderPlacementBlackBox(unittest.TestCase):
    def test_add_and_remove_item(self):
        cart = Cart()
        cart.add_item("Burger", 8.99, 1)
        self.assertEqual(len(cart.items), 1)
        cart.remove_item("Burger")
        self.assertEqual(len(cart.items), 0)

    def test_order_placement(self):
        cart = Cart()
        user_profile = UserProfile(delivery_address="123 Main St")
        restaurant_menu = RestaurantMenu(available_items=["Burger", "Pizza"])
        order_placement = OrderPlacement(cart, user_profile, restaurant_menu)
        cart.add_item("Burger", 8.99, 1)
        result = order_placement.validate_order()
        self.assertTrue(result["success"])

if __name__ == '__main__':
    unittest.main()