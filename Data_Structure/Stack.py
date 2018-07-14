#! /usr/bin/env python3
"""Stack -
    1. pop - Worst/Best O(1).
    2. push. Worst/Best O(1).
    Can be implement with LinkedList using insertFront & Delete Front"""


class Stack:
    def __init__(self,size):
        self.stack = [None] * size
        self.size = 0
        self.max_size = len(self.stack)

    def push(self,data):
        if (self.size < self.max_size):
            self.stack[self.size] = data
            self.size += 1
        else:
            return "over flow"

    def pop(self):
        if (self.size > 0):
            poped = self.stack[self.size -1]
            self.stack[self.size - 1] = None
            self.size = self.size - 1
            return poped
        else:
            return "under flow"

    def print(self):
        print(self.stack)
