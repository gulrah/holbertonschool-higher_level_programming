#!/usr/bin/python3
"""Module for Base class."""
import json
import os


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list object."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, mode="r", encoding="utf-8") as file:
            return [cls.create(**d) for d in cls.from_json_string(file.read())]

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def to_dictionary(list_dictionaries):
        """Return the dictionary representation of a list of dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return [dict(obj) for obj in list_dictionaries]


class Rectangle(Base):
    """Class Rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Y getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """Return the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Print in stdout the Rectangle instance with the character #."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Override the str method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}


class Square(Rectangle):
    """Class Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Override the str method."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
