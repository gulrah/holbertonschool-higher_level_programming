#!/usr/bin/python3

def roman_to_int(x):
    if not isinstance(x, str) or x is None:
        return 0
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0
    for char in reversed(x):
        current_value = roman_numerals.get(char, 0)
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value
    return result
