#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

from __future__ import print_function
from __future__ import unicode_literals
from builtins import input
import random

secret = random.randint(1, 100)
guess = 0

print("你好, 你很幸运, 我是一个路过的神仙, 我有一个秘密!")
print("我的秘密是一个从1到99的数字, 我只会给你6次机会来猜。")
print("如果你猜到它, 那说明你真的很幸运, 赶紧去买彩票吧!")

while guess != secret:
    print("你猜这个数字是多少? (1-100)")
    guess = int(input())
    if guess == secret:
        print("哇~~~, 真的假的！你居然发现了我的秘密! 它就是: ", str(secret))
        break
    elif guess < secret:
        print(str(guess),"太小了, 你还差点运气! ")
    elif guess > secret:
        print(str(guess),"太大了, 你还差点运气! ")
