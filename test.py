import unittest
from work import is_prime

class PrimeTestCase (unittest.TestCase):
    """Tests for `work.py`."""
    def test_is_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_four_is_prime(self):
        """Is four successfully determined to be prime?"""
        """If the test fails the message wil be displayed"""
        self.assertFalse(is_prime(4), msg='Four is not a prime number')   

    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))    

    def test_is_negative_prime(self):
        """Is a negative number correctly determined not to be prime?"""
        self.assertFalse(is_prime(-1), msg='negative is not a prime number')    

if __name__ == '__main__':
    unittest.main()