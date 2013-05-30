# -*- coding:utf-8 -*-
'''
다음 두 블로그를 참조
http://erezsh.wordpress.com/2012/11/18/how-to-write-a-calculator-in-50-python-lines-without-eval/
http://blog.83rpm.com/archives/882
'''
import re


def MyCalc(exp):
    def calculator(syms):
        if len(syms) == 3:
            return calc(syms)

        if '(' in syms:
            left = syms[::-1].index('(')
            right = syms.index(')')
            result = calculator(syms[-left:right])
            syms.insert(-left-1, str(result))
            del syms[-left-1:right+2]
            return calculator(syms)

        index = 1  # 순차 계산일 경우

        # 우선순위에 따라
        if '*' in syms:
            index = syms.index('*')

        if '/' in syms:
            index = syms.index('/')

        result = calc(syms[index-1:index+2])
        del syms[index-1:index+2]
        syms.insert(index-1, str(result))
        return calculator(syms)

    def calc(syms):
        if '*' in syms:
            return int(syms[0]) * int(syms[2])
        if '/' in syms:
            return int(syms[0]) / int(syms[2])
        if '+' in syms:
            return int(syms[0]) + int(syms[2])
        if '-' in syms:
            return int(syms[0]) - int(syms[2])


    symbols = re.findall('[[\d.]+|\(|\)|\+|\-|\/|\*|]', exp)
    return calculator(symbols)
