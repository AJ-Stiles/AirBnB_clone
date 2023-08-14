#!/usr/bin/python3
"""
Unittests for Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class.
    """

    def test_attributes(self):
        """Test Review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "id"))


if __name__ == "__main__":
    unittest.main()
