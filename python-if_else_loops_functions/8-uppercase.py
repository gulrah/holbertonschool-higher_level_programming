#!/usr/bin/python3
def uppercase(str):
    result = ''
    for x in str:
        if ord('a') <= ord(x) <= ord('z'):
            result +=chr(ord(x) - 32)
        else:
            result += x
    print("{}".format(result))
