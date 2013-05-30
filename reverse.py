# -*- coding:utf-8 -*-


# 파이썬에는 reversed 함수가 있지만 사용하지 않고 구현해 보았습니다.
def reverse(string):
    new_string = ""
    for s in string:
        new_string = s + new_string
    return new_string
