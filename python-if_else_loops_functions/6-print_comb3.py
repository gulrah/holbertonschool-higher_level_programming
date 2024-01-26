#!/usr/bin/python3
for x in range (10):
    for y in range(x + 1, 10):
        sep = ", " if x < 8 or y < 9 else "\n"
        print("{}{}".format(x, y), end=sep)
