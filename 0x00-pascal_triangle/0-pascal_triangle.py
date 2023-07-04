#!/usr/bin/python3
"""This module defines a function that generates Pascal's Triangle."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    """

    if n <= 0:
        return []  # Return an empty list for invalid input

    result = [[1]]  # Initialize Pascal's Triangle with the first row [1]

    for i in range(n - 1):
        # Calculate the next row of Pascal's Triangle based on the previous row
        temp = [0] + result[-1] + [0]  # Add padding of zeros to handle edge elements
        next_row = []
        for j in range(len(result[-1]) + 1):
            # Calculate each element in the next row by summing adjacent elements in the previous row
            next_row.append(temp[j] + temp[j + 1])
        result.append(next_row)  # Add the next row to Pascal's Triangle

    return result

