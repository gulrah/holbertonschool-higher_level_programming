#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
        """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): Input text

    Raises:
        TypeError: If text is not a string
    """
            if not isinstance(text, str):
                        raise TypeError("text must be a string")

                        separators = [".", "?", ":"]
                            for char in text:
                                        print(char, end="")
                                                if char in separators:
                                                                print("\n")
                                                                
