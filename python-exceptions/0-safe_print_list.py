#!/usr/bin/python3
def safe_print_list(a=[], b=0):
    c = 0
    try:
        for i in range(b):
            print(a[i], end='')
            c += 1
    except IndexError:
        pass
    finally:
        print()
    return c
