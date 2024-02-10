#!/usr/bin/python3
"""
Returns an object represented by a JSON string.
"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    import json
    return json.loads(my_str)


if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))
