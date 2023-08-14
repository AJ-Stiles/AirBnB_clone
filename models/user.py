#!/usr/bin/python3
"""
User module: Defines the User class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class inherits from BaseModel and defines user attributes.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)

