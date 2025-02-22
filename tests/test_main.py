import unittest
from src.main import fetch_quote

class TestMotivator(unittest.TestCase):
    def test_fetch_quote(self):
        """Test that fetch_quote returns a string containing a quote."""
        quote = fetch_quote()
        self.assertIsInstance(quote, str)
        self.assertTrue(len(quote) > 10)

if __name__ == "__main__":
    unittest.main()
