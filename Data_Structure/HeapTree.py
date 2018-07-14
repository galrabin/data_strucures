#!/usr/bin/env python3
import math


class BinaryHeap:
    def __init__(self,size):
        self.size = size + 1
        self.arr = [None] * (self.size)
        self.last = -1

    def insert(self,data):
        self.last += 1
        self.arr[self.last] = data
        self.percolateUp(self.last)

    def swap(self,i,j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def percolateUp(self,child):
        if child == 0:
            return
        if child % 2 == 0:
            parent = int(child / 2)
        else:
            parent = int((child - 1) / 2)
        if self.arr[parent] > self.arr[child]:
            self.swap(parent,child)
            self.percolateUp(parent)
        else:
            return


    def percolateDown(self,currentRoot):
        while (2 * currentRoot < self.last):
            min_child = self.min_child(currentRoot)
            if self.arr[currentRoot] > self.arr[min_child]:
                self.swap(currentRoot,min_child)
            currentRoot = min_child


    def min_child(self,i):
        if i * 2 + 1 < self.last:
            if self.arr[i * 2] > self.arr[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2
        else:
            return i * 2


    def delMin(self):
        if self.last > 0:
            min = self.arr[0]
            self.arr[0] = self.arr[self.last]
            self.arr[self.last] = None
            self.last -= 1
            self.percolateDown(0)
            return min
        else:
            return "Over flow"

    def print(self):
        print(arr)



def build_heap(arr):
    newArr = BinaryHeap(len(arr))
    newArr.arr = arr.copy()
    nodes = len(arr)
    junctions = int(nodes / 2)
    if nodes % 2 != 0:
        junctions += 1
    for i in range(junctions+1):
        print(junctions - i)
        newArr.percolateDown(junctions - i)
    return newArr




