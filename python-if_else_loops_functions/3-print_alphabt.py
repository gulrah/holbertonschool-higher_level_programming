#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if chr(x) not in ('qe'):
        print("{}".format(chr(x)), end='')
