import unittest
from test_Order_Placement import Cart

class TestOrderPlacementWhiteBox(unittest.TestCase):
    def test_update_item_quantity(self):
        cart = Cart()
        cart.add_item("Burger", 8.99, 1)
        cart.update_item_quantity("Burger", 2)
        self.assertEqual(cart.items[0].quantity, 2)

    def test_calculate_total(self):
        cart = Cart()
        cart.add_item("Burger", 8.99, 2)
        cart.add_item("Pizza", 12.99, 1)
        total = cart.calculate_total()
        self.assertEqual(total["total"], 8.99 * 2 + 12.99 + 0.10 * (8.99 * 2 + 12.99) + 5.00)

if __name__ == '__main__':
    unittest.main()