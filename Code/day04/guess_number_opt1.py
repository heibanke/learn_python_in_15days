#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

from __future__ import print_function
from __future__ import unicode_literals
from builtins import input
import random

secret = random.randint(1, 100)

# 增加tries，统计猜的次数
guess,tries = 0,0

print("你好, 你很幸运, 我是一个路过的神仙, 我有一个秘密!")
print("我的秘密是一个从1到99的数字, 我只会给你6次机会来猜。")
print("如果你猜到它, 那说明你真的很幸运, 赶紧去买彩票吧!")

# 增加条件判断猜的次数
while guess != secret and tries <= 6:
    print("你猜这个数字是多少? (1-100)")
    guess = int(input())
    if guess == secret:
        print("哇~~~, 真的假的！你居然发现了我的秘密! 它就是: ", str(secret))
        break
    elif guess < secret:
        print(str(guess),"太小了, 你还差点运气! ")
    elif guess > secret:
        print(str(guess),"太大了, 你还差点运气! ")

    # 每次猜的次数要累加
    tries += 1

else:
    # 超过猜的次数的输出
    print("你唯一的机会已被你用完了！看来你还需要再攒点人品！")
    print("还是让我告诉你吧！这个数字是: ", str(secret))