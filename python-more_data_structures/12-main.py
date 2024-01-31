def roman_to_int(roman_string):
    # Dictionary mapping Roman numerals to their integer values
    roman_values = {'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000}

      # Check if the input is a string or None
      if not isinstance(roman_string, str) or roman_string is None:
           return 0

            # Initialize result
              result = 0

                  # Iterate through the Roman string
                  for i in range(len(roman_string)):
                       # If current value is smaller than the next value,
                       # subtract it
                       if i < len(
                           roman_string) - 1 and roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]:
                            result -= roman_values[roman_string[i]]
                        else:
                            result += roman_values[roman_string[i]]

                              return result

                            # Example usage:
                            roman_number = "X"
                            print("{} = {}".format(roman_number,
                                  roman_to_int(roman_number)))

                            roman_number = "VII"
                            print("{} = {}".format(roman_number,
                                  roman_to_int(roman_number)))

                            roman_number = "IX"
                            print("{} = {}".format(roman_number,
                                  roman_to_int(roman_number)))

                            roman_number = "LXXXVII"
                            print("{} = {}".format(roman_number,
                                  roman_to_int(roman_number)))

                            roman_number = "DCCVII"
                            print("{} = {}".format(roman_number,
                                  roman_to_int(roman_number)))
