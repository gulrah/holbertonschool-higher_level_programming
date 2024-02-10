#!/usr/bin/python3
def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]  # First element in every row is 1
        if triangle:
            last_row = triangle[-1]
            # Calculate each element in the current row (excluding the first and last element)
            # by summing the corresponding elements from the previous row
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # Last element in every row is 1
        triangle.append(row)

    return triangle
