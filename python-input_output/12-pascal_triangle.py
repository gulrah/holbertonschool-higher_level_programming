#!/usr/bin/python3
'''
class Student
'''


class Student:
    '''
    class that defines a student by first_name, last_name, and age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})
