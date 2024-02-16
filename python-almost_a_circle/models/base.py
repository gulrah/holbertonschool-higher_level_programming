#!/usr/bin/python3
"""Module for Base class."""
import json


class Base:
    """Base class for managing id attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
           file.write(cls.to_json_string([
    obj.to_dictionary() for obj in list_objs
]))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)  # Create a "dummy" instance
        elif cls.__name__ == "Square":
            new_instance = cls(1)  # Create a "dummy" instance
        new_instance.update(**dictionary)  # Apply the real values
        return new_instance


class Rectangle(Base):
    """Rectangle class inheriting from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """Update attributes of the Rectangle."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


class Rectangle(Base):
    """Rectangle class inheriting from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """Update attributes of the Rectangle."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
