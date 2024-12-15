import unittest
from test_User_Registration import UserRegistration

class TestUserRegistrationBlackBox(unittest.TestCase):
    def test_successful_registration(self):
        registration = UserRegistration()
        result = registration.register("user@example.com", "StrongPassword123", "StrongPassword123")
        self.assertTrue(result['success'])

    def test_email_already_registered(self):
        registration = UserRegistration()
        registration.register("user@example.com", "StrongPassword123", "StrongPassword123")
        result = registration.register("user@example.com", "AnotherPassword", "AnotherPassword")
        self.assertFalse(result['success'])

if __name__ == '__main__':
    unittest.main()