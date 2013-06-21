# -*- coding:utf-8 -*-
# 문자열 뒤집기


def reverse(string):
    new_string = ""
    for s in string:
        new_string = s + new_string
    return new_string
