class UserRegistration:
    def __init__(self):
        """
        Initializes the UserRegistration class with an empty dictionary to store user data.
        Each entry in the dictionary will map an email to a dictionary containing the user's password and confirmation status.
        """
        self.users = {}

    def register(self, email, password, confirm_password):
        """
        Registers a new user.

        This function takes an email, password, and password confirmation as input. It performs a series of checks to ensure the registration
        is valid:
        - Verifies that the email is in a valid format.
        - Ensures that the password matches the confirmation password.
        - Validates that the password meets the strength requirements.
        - Checks if the email is already registered.

        If all checks pass, the user is registered, and their email and password are stored in the `users` dictionary, along with a confirmation
        status set to False (indicating the user is not yet confirmed). A success message is returned.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            confirm_password (str): Confirmation of the user's password.

        Returns:
            dict: A dictionary containing the result of the registration attempt.
                  On success, it returns {"success": True, "message": "Registration successful, confirmation email sent"}.
                  On failure, it returns {"success": False, "error": "Specific error message"}.
        """
        if email is None or not isinstance(email, str) or not self.is_valid_email(email):
            return {"success": False, "error": "Invalid email format"}
        if password is None or not isinstance(password, str) or len(password) == 0:
            return {"success": False, "error": "Password is required"}
        if confirm_password is None or not isinstance(confirm_password, str) or len(confirm_password) == 0:
            return {"success": False, "error": "Password confirmation is required"}
        if password != confirm_password:
            return {"success": False, "error": "Passwords do not match"}
        if not self.is_strong_password(password):
            return {"success": False, "error": "Password is not strong enough"}
        if email in self.users:
            return {"success": False, "error": "Email already registered"}

        self.users[email] = {"password": password, "confirmed": False}
        return {"success": True, "message": "Registration successful, confirmation email sent"}

    def is_valid_email(self, email):
        """
        Checks if the provided email is valid based on a simple validation rule.
        This rule only checks that the email contains an '@' symbol and has a '.' in the domain part.

        Args:
            email (str): The email address to be validated.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        if email is None or not isinstance(email, str):
            return False
        return "@" in email and "." in email.split("@")[-1]

    def is_strong_password(self, password):
        """
        Checks if the provided password meets the strength requirements.
        A strong password is defined as one that is at least 8 characters long, contains at least one letter, and at least one number.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password is strong, False otherwise.
        """
        if password is None or not isinstance(password, str) or len(password) == 0:
            return False
        return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)


import unittest


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.registration = UserRegistration()

    def test_successful_registration(self):
        result = self.registration.register("user@example.com", "Password123", "Password123")
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], "Registration successful, confirmation email sent")

    def test_invalid_email(self):
        result = self.registration.register("userexample.com", "Password123", "Password123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Invalid email format")

    def test_password_mismatch(self):
        result = self.registration.register("user@example.com", "Password123", "Password321")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Passwords do not match")

    def test_weak_password(self):
        result = self.registration.register("user@example.com", "pass", "pass")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Password is not strong enough")

    def test_email_already_registered(self):
        self.registration.register("user@example.com", "Password123", "Password123")
        result = self.registration.register("user@example.com", "Password123", "Password123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Email already registered")

    def test_empty_email(self):
        result = self.registration.register("", "Password123", "Password123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Invalid email format")

    def test_empty_password(self):
        result = self.registration.register("user@example.com", "", "Password123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Password is required")

    def test_empty_confirm_password(self):
        result = self.registration.register("user@example.com", "Password123", "")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Password confirmation is required")

    def test_email_none(self):
        result = self.registration.register(None, "Password123", "Password123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Invalid email format")

    def test_password_none(self):
        result = self.registration.register("user@example.com", None, "Password123")
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Password is required")

    def test_confirm_password_none(self):
        result = self.registration.register("user@example.com", "Password123", None)
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Password confirmation is required")


if __name__ == '__main__':
    unittest.main()