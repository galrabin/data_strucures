# /usr/bin/env python3
import Data_Structure.HeapTree

"""Swap two indexes in array"""
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

"""Insertion sort - sort an array.
    Best case = O(n)
    Worst case = O(n^2)
    Space = O(1)
    Arguments : array
    Return : Sorted array"""
def insertion_sort(arr):
    for i in range (1,len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = current
    return arr


"""Bubble sort - sort an array.
    Best case = O(n)
    Worst case = O(n^2)
    Space = O(1)
    Arguments : array
    Return : Sorted array"""
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            right = arr[j]
            left = arr[j-1]
            if left > right:
                arr[j-1] = right
                arr[j] = left
    return arr

"""HeapSort - sort an array.
    Best case = O(nlogn)
    Worst case = O(nlogn)
    Space = O(1)
    Arguments : array
    Return : Sorted array"""
def heap_sort(arr):
    bh = Data_Structure.HeapTree.build_heap(arr)
    for i in range(arr):
        arr[len(arr) - i] = bh.min_child()
    return bh

