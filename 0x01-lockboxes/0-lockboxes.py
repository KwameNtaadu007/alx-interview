#!/usr/bin/python3

"""
Python module for determing sequential algorithm using
boxes and keys.
"""

def canUnlockAll(boxes):
    """
    Funct to check if the boxes can unlock
    Args:
    boxes: list of lists
    Return: True or False
    """
    beginner = 0
    unlock = {}

    for eachbox in boxes:
        if len(eachbox) == 0 or beginner == 0:
            unlock[beginner] = "unlocked"
        for key in eachbox:
            if key < len(boxes) and key != beginner:
                unlock[key] = key
        if len(unlock) == len(boxes):
            return True
        beginner += 1
    return False
