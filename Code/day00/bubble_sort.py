#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke
"""
bubble sort alg

最上面的注释
# coding: utf-8
是为了声明文件编码类型，有中文的话，需要定义为utf-8
"""
from __future__ import print_function

# 冒泡算法的函数定义
def bubble_sort(nums):
    # 这个函数就是下面这些语句的打包。
    for j in range(len(nums)):
        for i in range(0,len(nums)-j-1,1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                print(nums)
        print('\n',j)



# 定义一组数，用list保存。list我们第三课会讲到。
numbers=[34, 9, 5, 23, 14, 7, 32, 2, 12]

# 调用冒泡算法函数，直接对numbers进行了排序
bubble_sort(numbers)

# 打印排序后的值
print(numbers)
