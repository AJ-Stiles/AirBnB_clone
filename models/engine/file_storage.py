#!/usr/bin/python3
"""
FileStorage module: Defines the FileStorage class for serializing and deserializing objects.
"""

import json

class FileStorage:
    """
    FileStorage class serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        module_name = "models.user"
                    elif class_name == 'State':
                        module_name = "models.state"
                    elif class_name == 'City':
                        module_name = "models.city"
                    elif class_name == 'Amenity':
                        module_name = "models.amenity"
                    elif class_name == 'Place':
                        module_name = "models.place"
                    elif class_name == 'Review':
                        module_name = "models.review"
                    else:
                        continue
                    module = __import__(module_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

