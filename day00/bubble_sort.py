#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke
"""
bubble sort alg
"""
from __future__ import print_function


def bubble_sort(nums):
    for j in range(len(nums)):
        for i in range(0,len(nums)-j-1,1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                print(nums)
        print('\n',j)




numbers=[34, 9, 5, 23, 14, 7, 32, 2, 12]
bubble_sort(numbers)
print(numbers)
