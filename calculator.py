# -*- coding:utf-8 -*-
'''
다음 블로그를 참조
http://erezsh.wordpress.com/2012/11/18/how-to-write-a-calculator-in-50-python-lines-without-eval/
'''
import re


def MyCalc(exp):
    def calculator(symbols, LPAR=0, RPAR=0):
        if '(' in symbols:
            LPAR = len(symbols) - symbols[::-1].index('(') - 1
            RPAR = symbols[LPAR:].index(')') + LPAR

            sub_symbols = symbols[LPAR+1:RPAR]
            del symbols[LPAR:RPAR+1]
            symbols.insert(LPAR, str(calculator(sub_symbols)))
            return calculator(symbols)

        if len(symbols) == 3:
            return operations(symbols)

        index = 1  # 순차 계산일 경우

        # 우선순위에 따라
        if '*' in symbols:
            index = symbols.index('*')

        if '/' in symbols:
            index = symbols.index('/')

        result = operations(symbols[index-1:index+2])
        del symbols[index-1:index+2]
        symbols.insert(index-1, result)
        return calculator(symbols)

    def operations(symbols):
        if '*' in symbols:
            return int(symbols[0]) * int(symbols[2])
        if '/' in symbols:
            return int(symbols[0]) / int(symbols[2])
        if '+' in symbols:
            return int(symbols[0]) + int(symbols[2])
        if '-' in symbols:
            return int(symbols[0]) - int(symbols[2])

    symbols = re.findall('[[\d.]+|\(|\)|\+|\-|\/|\*|]', exp)
    return calculator(symbols)
