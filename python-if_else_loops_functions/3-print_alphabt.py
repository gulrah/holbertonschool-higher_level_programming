#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if chr(x) not in ('q','e'):
        print("{}".format(chr(x)))
