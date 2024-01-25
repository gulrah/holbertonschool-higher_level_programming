#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if number < 0:
    number = number * (-1)
    lastdigit = number % 10
    number = number * (-1)
    lastdigit = lastdigit * (-1)
print(f"Last digit of {number} is {lastdigit}", end="")
if lastdigit == 0:
    print(f" and is 0")
elif lastdigit > 5:
    print(f" and is greater than 5")
else:
    print(f" and is less than 6 and not 0")
