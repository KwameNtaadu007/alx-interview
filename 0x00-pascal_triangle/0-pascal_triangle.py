#!/usr/bin/python3
"""
Python script to contain a function to generate a Pascal Triangle
"""


def pascal_triangle(n):
    """ Returning a list of lists of integers
    that represents the pascal's triangle of n. """
    rows = []
    if n <= 0:
        return rows

    for x in range(n):
        # Check if it's the first row
        if x == 0:
            rows.append([1])
            continue

        # copy the contents of the previous row
        prev = rows[x - 1].copy()

        # Declare a container for the new row and append 1
        row = []
        row.append(1)

        # Loop through the contents of the previous row, adding up
        # the value at index and value at next index
        y = 0
        while y < x - 1:
            row.append(prev[y] + prev[y + 1])
            y += 1

        # Append 1 and add to list of rows
        row.append(1)
        rows.append(row)

    return rows
