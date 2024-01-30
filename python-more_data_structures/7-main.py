def update_dictionary(a_dictionary, key, value):
    # Replace or add key/value in the dictionary
    a_dictionary[key] = value
          return a_dictionary

# Example usage:
      a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
      new_dict = update_dictionary(a_dictionary, 'language', "Python")
      print_sorted_dictionary(new_dict)
      print("--")
      print_sorted_dictionary(a_dictionary)

      print("--")
      print("--")

      new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
      print_sorted_dictionary(new_dict)
      print("--")
      print_sorted_dictionary(a_dictionary)
      
