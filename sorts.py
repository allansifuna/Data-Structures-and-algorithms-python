# -*- coding: utf-8 -*-
"""
Created on Sat March 21 12:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""

def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        more=[i for i in arr[1:] if i>pivot]
        print(less)
        print(more)
        return quickSort(less)+[pivot]+quickSort(more)

def findSmallest(arr):
    sm=arr[0]
    ind=0
    for i in range(len(arr)):
        if arr[i]<sm:
            sm=arr[i]
            ind=i
    return ind


def selectionSort(arr):
    new_arr=[]
    for i in range(len(arr)):
        new_arr.append(arr.pop(findSmallest(arr)))
    return new_arr
print(selectionSort([1,3,4,2,4,2,5,6,8,6,8,5]))

def binarySearch(arr,n):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        guess=arr[mid]
        if guess==n:
            return mid
        if guess>n:
            high=mid-1
        else:
            low=mid+1

print(binarySearch([1,2,3,4,5,6,7,8,9],8))
