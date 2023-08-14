#!/usr/bin/python3
"""
Unittests for Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class.
    """

    def test_attributes(self):
        """Test Amenity attributes."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "name"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "id"))


if __name__ == "__main__":
    unittest.main()
