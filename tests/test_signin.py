import unittest

from src import signin


class SignInTests(unittest.TestCase):
    def test_get_db_login(self):
        self.assertEqual(signin.get_db_login(), ("registrar", "admin"))

    def test_hash_password(self):
        self.assertEqual(signin.hash_password(" abc "), signin.hash_password("abc"))

    def test_normalize_roll_no(self):
        self.assertEqual(signin.normalize_roll_no(" cs123456 "), "CS123456")

    def test_build_email(self):
        self.assertEqual(
            signin.build_email(" CS123456 ", "uni.edu"), "cs123456@uni.edu"
        )

    def test_is_valid_roll_no(self):
        self.assertTrue(signin.is_valid_roll_no("cs123456"))
        self.assertFalse(signin.is_valid_roll_no("12345"))

    def test_mask_email(self):
        self.assertEqual(signin.mask_email("sara@uni.edu"), "sa***@uni.edu")

    def test_is_strong_password(self):
        self.assertTrue(signin.is_strong_password("abcd1234"))
        self.assertFalse(signin.is_strong_password("abcdefgh"))
