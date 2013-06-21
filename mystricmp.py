# -*- coding:utf-8 -*-
# 대소문자 상관없이 문자 순서 비교


def MyStricmp(a, b):
    lower_a = a.lower()
    lower_b = b.lower()
    if lower_a == lower_b:
        return 0
    if lower_a > lower_b:
        return 1
    if lower_a < lower_b:
        return -1
