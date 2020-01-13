#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:50:13 2019

@author: naotto
"""
import random
from datetime import datetime, date

def SelSort(num):
    steps = 0
    n = len(num)
    PastTime = (datetime.now().time())
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if num[mp] > num[i]:
                mp = i
        if mp != bottom:
            num[mp], num[bottom] = num[bottom], num[mp]
            steps += 1
    CurrentTime = (datetime.now().time())
    return num, steps, datetime.combine(date.today(), CurrentTime) - datetime.combine(date.today(), PastTime)


def TestSelectionSort(list_len, exp_count):
    average = 0
    for _ in range(exp_count):
        arr = []
        for i in range(list_len):
            arr.append(random.randint(0,1000))
        print("\nUnsorted array: %s" % arr)
        SortedArr, StepSwapping, Time= SelSort(arr)
        print("Sorted array: %s" % SortedArr)
        print("Steps of swapping: %d" % StepSwapping)
        print("Time:", Time)
        average += StepSwapping
    average = average / exp_count
        
#TestSelectionSort(10,1000)


def LinearSea(x, nums):
    steps = 0
    PastTime = (datetime.now().time())
    for i in range(len(nums)):
        steps += 1
        if nums[i] == x:
            CurrentTime = (datetime.now().time())
            return steps, datetime.combine(date.today(), CurrentTime) - datetime.combine(date.today(), PastTime)
    return -1


def BinarySea(x,nums):
    low = 0
    high = len(nums) - 1
    steps = 0
    PastTime = (datetime.now().time())
    while low <= high:
        steps += 1
        mid = (high+low) // 2
        item = nums[mid]
        if item == x:
            CurrentTime = (datetime.now().time())
            return steps, datetime.combine(date.today(), CurrentTime) - datetime.combine(date.today(), PastTime)
        elif item > x:
            high = mid - 1
        else:
            low = mid + 1
    CurrentTime = (datetime.now().time())
    return -1, datetime.combine(date.today(), CurrentTime) - datetime.combine(date.today(), PastTime)



def TestSearch(list_len, exp_count):
    for _ in range(exp_count):
        arr = []
        for i in range(list_len):
            arr.append(random.randint(0,1000))
        searching = random.choice(arr)
        print("\nUnsorted array: %s" % arr)
        print("Searching number: %d" % searching)
        LinearSearch, Time = LinearSea(searching, arr)
        print("\nSteps of Linear Searching: %d" % LinearSearch)
        print("Time:", Time)
        BinarySearch, Time = BinarySea(searching, arr)
        print("Steps of Binary Searching: %d" % BinarySearch)
        print("Time:", Time)
        SelSort(arr)
        LinearSearch, Time = LinearSea(searching, arr)
        print("\nSteps of Linear Searching with SelSort: %d" % LinearSearch)
        print("Time", Time)
        BinarySearch, Time = BinarySea(searching, arr)
        print("Steps of Binary Searching with SelSort: %d" % BinarySearch)
        print("Time:", Time)
        
#TestSearch(10,10)
        
s = "Jupiter Notebook"
index = len(s)-1
while index >= 0:
    print(s[index],end = "")
    index -= 1