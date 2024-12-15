import unittest
from test_Payment_Processing import PaymentProcessing

class TestPaymentProcessingBlackBox(unittest.TestCase):
    def test_process_payment_success(self):
        payment_processing = PaymentProcessing()
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        result = payment_processing.process_payment({"total_amount": 100.00}, "credit_card", payment_details)
        self.assertEqual(result, "Payment successful, Order confirmed")

    def test_process_payment_failure(self):
        payment_processing = PaymentProcessing()
        payment_details = {
            "card_number": "1111222233334444",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        result = payment_processing.process_payment({"total_amount": 100.00}, "credit_card", payment_details)
        self.assertEqual(result, "Payment failed, please try again")

if __name__ == '__main__':
    unittest.main()