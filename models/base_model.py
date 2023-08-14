#!/usr/bin/python3
"""
BaseModel module: Defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            args: Non-keyword arguments (not used in this implementation).
            kwargs: Keyword arguments to populate instance attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    if key != '__class__':
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        import models
        """Save the instance to the storage and call
        the storage save method."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict


if __name__ == '__main__':
    my_dict = {
        'id': '12345',
        'created_at': '2023-08-01T12:00:00.000000',
        'name': 'Sample Name',
        'my_number': 42
    }

    my_model = BaseModel(**my_dict)
    print(my_model)
