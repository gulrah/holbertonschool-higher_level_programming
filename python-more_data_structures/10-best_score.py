#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = max(a_dictionary, key=a_dictionary.get)
        return x
    else:
        return None
