#!/usr/bin/env python3

"""Count sort - sort an array.
    Best case = O(n)
    Worst case = O(n)
    Space = O(n)
    Arguments : Int array
    Return : Sorted array"""
def count_sort(arr, r):
    count = [0 for item in range(r + 1)]
    output = [0 for item in range(r + 1)]
    for item in arr:
        count[item] += 1
    for i in range(1,r+1):
        count[i] += count[i-1]
    for i in range(len(arr)):
        output[count[arr[i]]] = arr[i]
        count[arr[i]] -= 1
