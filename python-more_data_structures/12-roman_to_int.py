#!/usr/bin/python3
def roman_to_int(roman_string):
            if not isinstance(roman_string, str):
                            return 0

                        roman_dict = {"X": 10, "V": 5, "I": 1, "L": 50, "D": 500, "M": 1000, "C": 100}
                            result = 0

                                for i in range(len(roman_string)):
                                                value = roman_dict[roman_string[i]]
                                                        if i < len(roman_string) - 1 and roman_dict[roman_string[i + 1]] > value:
                                                                            result -= value
                                                        else:
                                                                            result += value

                                                                                return result
