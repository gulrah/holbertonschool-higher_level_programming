def simple_delete(a_dictionary, key=""):
    # Delete a key in the dictionary if it exists
a_dictionary.pop(key, None)
    return a_dictionary

# Example usage:
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
  new_dict = simple_delete(a_dictionary, 'track')
  print_sorted_dictionary(a_dictionary)
  print("--")
  print_sorted_dictionary(new_dict)

  print("--")
  print("--")
  new_dict = simple_delete(a_dictionary, 'c_is_fun')
  print_sorted_dictionary(a_dictionary)
  print("--")
  print_sorted_dictionary(new_dict)
  
