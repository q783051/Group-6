import unittest
from test_User_Registration import UserRegistration

class TestUserRegistrationWhiteBox(unittest.TestCase):
    def test_password_requirements(self):
        registration = UserRegistration()
        result = registration.register("user@example.com", "short", "short")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Password is not strong enough")

    def test_email_validation(self):
        registration = UserRegistration()
        result = registration.register("notanemail", "StrongPassword123", "StrongPassword123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Invalid email format")

if __name__ == '__main__':
    unittest.main()