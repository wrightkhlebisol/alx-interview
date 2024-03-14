#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Check if boxes can be unlocked."""
    opened_boxes = set()
    opened_boxes.add(0)

    def dfs(box_index):
        for key in boxes[box_index]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                dfs(key)

    dfs(0)

    return len(opened_boxes) == len(boxes)
