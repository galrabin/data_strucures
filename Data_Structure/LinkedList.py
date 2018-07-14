#!/usr/bin/env python3

"""Linked List using Nodes -
    Search:
    1. Best case = O(1)
    2. Worst Case = O(n)

    Remove:
    1. Best case = O(1)
    2. Worst Case = O(n)

    Insert:
    1. Best/Worst = O(1)
    
    DLL - Doubly linked list, just preserve the previous pointer.
    Linked List using array-Two array initiate:
    1. Data - value inserted.
    2. Next - pointer to the next node.""
    """

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove(self,value):
        prev = self.head
        current = prev
        for i in range(self.size):
            if current.data == value:
                prev.next = current.next
                self.size = self.size - 1
            else:
                prev = current
                current = current.next

    def search(self,value):
        current = self.head
        for i in range(self.size):
            if current.data == value:
                return i
            else:
                current = current.next
        return None

    def print(self):
        x = '['
        current = self.head
        for i in range(self.size):
            x += str(current.data)
            current = current.next
            if i < self.size - 1:
                x += ','
        x += ']'
        print(x)



