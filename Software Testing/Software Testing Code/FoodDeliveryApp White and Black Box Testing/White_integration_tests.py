import unittest
from integration_tests import UserRegistration

class TestIntegrationWhiteBox(unittest.TestCase):
    def test_email_already_registered(self):
        registration = UserRegistration()
        registration.register("test@example.com", "password123", "password123")
        result = registration.register("test@example.com", "password123", "password123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Email already registered")

    def test_password_mismatch(self):
        registration = UserRegistration()
        result = registration.register("test@example.com", "password123", "password")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Passwords do not match")

if __name__ == '__main__':
    unittest.main()