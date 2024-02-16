#!/usr/bin/python3

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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            instance = cls(1, 1)  # Create a dummy instance
        else:
            instance = cls(1)  # Create a dummy instance
        instance.update(**dictionary)
        return instance

    def update(self, *args, **kwargs):
        """Assigns attributes."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

class Rectangle(Base):
    """Rectangle class, inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

class Square(Rectangle):
    """Square class, inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

if __name__ == "__main__":
    r = Rectangle.create(**{'width': 2, 'height': 3})
    print(r.to_dictionary())
    r2 = Rectangle.create(**{'width': 2, 'height': 3, 'x': 12})
    print(r2.to_dictionary())
    r3 = Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1})
    print(r3.to_dictionary())
    r4 = Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89})
    print(r4.to_dictionary())
    s = Square.create(**{'size': 2})
    print(s.to_dictionary())
    s2 = Square.create(**{'size': 2, 'x': 1})
    print(s2.to_dictionary())
    s3 = Square.create(**{'size': 2, 'x': 1, 'y': 3})
    print(s3.to_dictionary())
    s4 = Square.create(**{'size': 2, 'x': 1, 'y': 3, 'id': 89})
    print(s4.to_dictionary())
