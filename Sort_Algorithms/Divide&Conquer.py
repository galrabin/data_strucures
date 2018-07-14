#!/usr/bin/env python3
"""merge sort - sort an array.
    Best case = O(nlogn)
    Worst case = O(nlogn)
    Space = O(n)
    Arguments : array
    Return : Sorted array"""
def merge_sort(arr,first,last):
    if first < last:
        median  = int((first + last) / 2)
        merge_sort(arr, first, median)
        merge_sort(arr, median + 1, last)
        merge(arr, first, median, last)

def merge(arr, first, median, last):
    arr1 = arr[first:median]
    arr2 = arr[median + 1:first]
    for i  in range(median,last,2):
        if arr1[i] < arr2[i]:
            arr[i] = arr1[i]
            arr[i+1] = arr2


"""Quick sort - sort an array.
    Best case = O(nlogn)
    Worst case = O(nlogn)
    Space = O(n)
    Arguments : array
    Return : Sorted array"""

def median(arr,left,right):
    med = int((left + right)/2)
    x = arr[left]
    y = arr[right]
    z = arr[med]
    minimum = min(x,y,z)
    maximum = max(x,y,z)
    arr[right] = maximum
    if x != minimum and x != maximum:
        arr[left]= arr[right-1]
        arr[right-1] = x
    if y != minimum and y != maximum:
        arr[right] = arr[right - 1]
        arr[right-1] = y
    if z != minimum and z != maximum:
        arr[med] = arr[right - 1]
        arr[right-1] = z


def partition(arr,left,right):
    median(arr,left,right)
    pivot = arr[right - 1]
    i = left
    j = right - 2
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        else:
            arr[right-1] = arr[j+1]
            arr[j+1] = pivot
            return j + 1


def quickSort(arr,left,right):
    if (right - left) > 1:
        q = partition(arr,left,right)
        quickSort(arr,left,q-1)
        quickSort(arr,q + 1,right)


def quickSort_median(arr):
    quickSort(arr,0,len(arr) - 1)
