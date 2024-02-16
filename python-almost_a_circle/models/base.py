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
        instance = cls.__new__(cls)
        instance.__dict__.update(dictionary)
        return instance

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

if __name__ == "__main__":
    r = Rectangle.create(**{'width': 2, 'height': 3})
    print(r.to_dictionary())
