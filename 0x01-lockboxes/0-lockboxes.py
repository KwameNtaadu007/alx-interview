#!/usr/bin/python3
"""
Python module for determing sequential algorithm using
boxes and keys.
"""
def canUnlockAll(boxes):
    """Function checks whether all boxes can be opened 
    or not
    """
    n = len(boxes)
    opened_boxes = [False] * n
    opened_boxes[0] = True
    next_box = [0]

    while next_box:
        current_box = next_box.pop()

        for item in boxes[current_box]:
            if not opened_boxes[item]:
                opened_boxes[item] = True
                next_box.append(item)

    return all(opened_boxes)
