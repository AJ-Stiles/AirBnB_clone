#!/usr/bin/python3
"""
Unittests for State class.
"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for State class.
    """

    def test_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "name"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "id"))

if __name__ == "__main__":
    unittest.main()

