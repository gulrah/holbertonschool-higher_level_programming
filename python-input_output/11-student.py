#!/usr/bin/python3
class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the student object to a JSON-compatible dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include in the JSON output.

        Returns:
            dict: A dictionary representation of the student object.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Reload the student object attributes from a JSON-compatible dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs to reload.
        """
        for key, value in json.items():
            setattr(self, key, value)
