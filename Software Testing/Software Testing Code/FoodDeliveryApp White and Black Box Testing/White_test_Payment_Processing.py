import unittest
from test_Payment_Processing import PaymentProcessing

class TestPaymentProcessingWhiteBox(unittest.TestCase):
    def test_validate_payment_method(self):
        payment_processing = PaymentProcessing()
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        try:
            payment_processing.validate_payment_method("credit_card", payment_details)
        except ValueError:
            self.fail("validate_payment_method raised ValueError unexpectedly")

    def test_validate_credit_card(self):
        payment_processing = PaymentProcessing()
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        self.assertTrue(payment_processing.validate_credit_card(payment_details))

if __name__ == '__main__':
    unittest.main()