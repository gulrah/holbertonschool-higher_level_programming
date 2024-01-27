#!/usr/bin/python3
def uppercase(str):
    result = ''
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            result += chr(ord(x) - 32)
        else:
            result += x
    print(result, end='\n')
