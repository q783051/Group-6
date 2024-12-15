import unittest
from test_Restaurant_Browsing import RestaurantBrowsing, RestaurantDatabase
from test_User_Registration import UserRegistration
from test_Order_Placement import OrderPlacement, Cart, UserProfile, RestaurantMenu, PaymentMethod
from test_Payment_Processing import PaymentProcessing

class User_registration_database_persistence_Test(unittest.TestCase):
    def setUp(self):
        self.registration = UserRegistration()

    def test_registration_with_persistence(self):
        # Test successful registration
        result = self.registration.register("user@example.com", "StrongPassword123", "StrongPassword123")
        self.assertTrue(result['success'])
        # Check if user is stored in the dictionary
        self.assertIn("user@example.com", self.registration.users)
        self.assertFalse(self.registration.users["user@example.com"]["confirmed"])

        # Test email already registered
        result = self.registration.register("user@example.com", "AnotherPassword123", "AnotherPassword123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Email already registered")


class Order_issuance_payment_processing_Test(unittest.TestCase):
    def setUp(self):
        # 初始化必要的组件
        self.restaurant_menu = RestaurantMenu(available_items=["Burger", "Pizza", "Salad"])
        self.user_profile = UserProfile(delivery_address="123 Main St")
        self.cart = Cart()
        self.order_placement = OrderPlacement(self.cart, self.user_profile, self.restaurant_menu)
        self.payment_processing = PaymentProcessing()

    def test_order_placement_and_payment_processing(self):
        # 添加商品到购物车
        self.cart.add_item("Burger", 8.99, 1)
        self.cart.add_item("Pizza", 12.99, 1)

        # 验证订单
        order_validation = self.order_placement.validate_order()
        self.assertTrue(order_validation["success"])

        # 准备结账
        checkout_info = self.order_placement.proceed_to_checkout()
        self.assertIn("items", checkout_info)
        self.assertIn("total_info", checkout_info)
        self.assertIn("delivery_address", checkout_info)

        # 从 checkout_info 中获取总金额
        total_amount = checkout_info["total_info"]["total"]

        # 处理支付
        payment_method = PaymentMethod()
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        # 确保 payment_processing.process_payment 方法接受正确的参数
        payment_result = self.payment_processing.process_payment({
            "total_amount": total_amount
        }, "credit_card", payment_details)
        self.assertEqual(payment_result, "Payment successful, Order confirmed")

        # 确认订单
        confirm_order_result = self.order_placement.confirm_order(payment_method)
        self.assertTrue(confirm_order_result["success"])
        self.assertEqual(confirm_order_result["message"], "Order confirmed")


class Consistency_between_restaurant_browsing_order_placement_Test(unittest.TestCase):
    def setUp(self):
        self.database = RestaurantDatabase()
        self.browsing = RestaurantBrowsing(self.database)

    def test_restaurant_search_consistency(self):
        # Search for Italian restaurants
        italian_restaurants = self.browsing.search_by_cuisine("Italian")
        self.assertGreater(len(italian_restaurants), 0)

        # Check if the first restaurant is indeed Italian
        self.assertEqual(italian_restaurants[0]['cuisine'], "Italian")






if __name__ == '__main__':
    unittest.main()

