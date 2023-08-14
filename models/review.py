#!/usr/bin/python3
"""
Review module: Defines the Review class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel and defines review attributes.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)

