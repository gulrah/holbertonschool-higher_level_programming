#!/usr/bin/python3
def uppercase(s):
    for char in s:
        uppercase_char = chr(ord(char) - 32) if ord('a') <= ord(char) <= ord('z') else char
        print("{}".format(uppercase_char), end="")
    print()
                                
