#!/usr/bin/python3
"""
City module: Defines the City class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel and defines city attributes.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
