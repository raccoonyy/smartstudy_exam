# -*- coding:utf-8 -*-


def MyFactorial(n):
    if n == 0 or n == 1:
        return 1
    if n >= 2:
        return MyFactorial(n-1) * n
