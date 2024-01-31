def best_score(a_dictionary):

    # Return the key with the biggest integer value or None if no score found
return max(a_dictionary, key=a_dictionary.get, default=None)

# Example usage:
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
