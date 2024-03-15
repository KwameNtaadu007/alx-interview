#!/usr/bin/python3
""" Bash script to determine if a box will open with a list
of keys stored in boxes that contain list of lists """


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

