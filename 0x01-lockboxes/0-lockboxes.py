#!/usr/bin/python3
"""
This is checking if all the boxes can be opened
"""


def canUnlockAll(boxes):

    def get_key(box):
        for key in box:
            keys.add(key)

    opened = {0}
    keys = set(boxes[0])

    while len(keys):
        key = keys.pop()
        if key not in opened and key < len(boxes):
            opened.add(key)
            get_key(boxes[key])

    return len(opened) == len(boxes)
