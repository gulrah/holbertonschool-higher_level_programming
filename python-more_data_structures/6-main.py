def print_sorted_dictionary(a_dictionary):
    # Print the dictionary by ordered keys
for key in sorted(a_dictionary.keys()):
print("{}: {}".format(key, a_dictionary[key]))

# Example usage:
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
  print_sorted_dictionary(a_dictionary)
    
