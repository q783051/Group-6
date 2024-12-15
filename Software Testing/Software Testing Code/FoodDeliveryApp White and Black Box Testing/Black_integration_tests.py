import unittest
from integration_tests import UserRegistration, OrderPlacement, Cart, UserProfile, RestaurantMenu, PaymentProcessing

class TestIntegrationBlackBox(unittest.TestCase):
    def test_registration(self):
        registration = UserRegistration()
        result = registration.register("test@example.com", "password123", "password123")
        self.assertTrue(result['success'])

    def test_order_placement_and_payment(self):
        cart = Cart()
        user_profile = UserProfile(delivery_address="123 Main St")
        restaurant_menu = RestaurantMenu(available_items=["Burger", "Pizza"])
        order_placement = OrderPlacement(cart, user_profile, restaurant_menu)
        payment_processing = PaymentProcessing()

        cart.add_item("Burger", 8.99, 1)
        checkout_info = order_placement.proceed_to_checkout()
        total_amount = checkout_info["total_info"]["total"]
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        payment_result = payment_processing.process_payment({
            "total_amount": total_amount
        }, "credit_card", payment_details)
        self.assertEqual(payment_result, "Payment successful, Order confirmed")

if __name__ == '__main__':
    unittest.main()