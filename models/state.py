#!/usr/bin/python3
"""
State module: Defines the State class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel and defines state attributes.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
