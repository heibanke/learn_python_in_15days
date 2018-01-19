#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke
"""
bubble sort alg
"""
from __future__ import print_function

def bubble_sort(nums):
    """
    bubble sort function
    input: list
    output: sorted list
    """
    n = nums[:]
    for j in range(len(n)):
        for i in range(len(n) - j - 1):
            if n[i] > n[i + 1]:
                n[i], n[i + 1] = n[i + 1],n[i]
                print(n)
        print('\n', j)
    return n

if __name__ == '__main__':
    numbers=[34, 9, 5, 23, 14, 7, 32, 2, 12]
    sorted_nums = bubble_sort(numbers)
    print('After sorted: ', sorted_nums)
    print('Before sorted: ', numbers)
    help(bubble_sort)
