# -*- coding:utf-8 -*-
# 팩토리얼 구하기


def MyFactorial(n):
    if n == 0 or n == 1:
        return 1
    if n >= 2:
        return MyFactorial(n-1) * n
