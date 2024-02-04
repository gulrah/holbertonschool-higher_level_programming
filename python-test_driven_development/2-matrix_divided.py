#!/usr/bin/python3
"""
Module for matrix division
"""


def matrix_divided(matrix, div):
        """
    Divides all elements of a matrix

    Args:
        matrix (list): List of lists of integers or floats
        div (int or float): Divisor

    Returns:
        list: New matrix with elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                    or if div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    """
            if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

                        if not all(isinstance(num, (int, float)) for row in matrix for num in row):
                                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

                                    if not isinstance(div, (int, float)):
                                                raise TypeError("div must be a number")

                                                if div == 0:
                                                            raise ZeroDivisionError("division by zero")

                                                            return [[round(num / div, 2) for num in row] for row in matrix]
                                                        
