#!/usr/bin/python3
"""
Amenity module: Defines the Amenity class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel and defines amenity attributes.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
