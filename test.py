#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from round import MyRound
from factorial import MyFactorial
from reverse import reverse
from mystricmp import MyStricmp
from calculator import MyCalc
from calculator2 import MyCalc2


# 소수를 받아 반올림한 정수를 반환
class TestMyRound(unittest.TestCase):
    def testRound(self):
        self.assertEqual(MyRound(10.01), 10)
        self.assertEqual(MyRound(10.61), 11)


# 팩토리얼 구하기
class TestMyFactorial(unittest.TestCase):
    def testFactorial(self):
        self.assertEqual(MyFactorial(1), 1)
        self.assertEqual(MyFactorial(2), 2)
        self.assertEqual(MyFactorial(3), 6)
        self.assertEqual(MyFactorial(5), 120)
        self.assertEqual(MyFactorial(10), 3628800)


# 문자열 뒤집기
class TestReverse(unittest.TestCase):
    def setUp(self):
        self.string = 'test_string'

    def testReverse(self):
        self.assertEqual(reverse(self.string), "".join(reversed(self.string)))


# 대소문자 상관없이 문자 순서 비교
class TestMyStricmp(unittest.TestCase):
    def setUp(self):
        self.a = 'ABc'
        self.b = 'aBC'
        self.c = 'abd'

    def testMyStricmp(self):
        self.assertEqual(MyStricmp(self.a, self.b), 0)
        self.assertEqual(MyStricmp(self.b, self.c), -1)
        self.assertEqual(MyStricmp(self.c, self.a), 1)


# 간단한 계산기(수식은 모두 올바르게 입력되었다고 가정)
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.exp1 = '3 + 1'
        self.exp2 = '3 + 4 - 2'
        self.exp3 = '((2 + 5) * 3) -2'
        self.exp4 = '3 + 6 / 4 * ( 2 - 5 )'
        self.exp5 = '10 + ( 2 + 5 * ( 3 - 1 ) * 2 ) * 6'
        self.exp6 = '( 10 + 2 ) + 5 * (( 3 - 1 ) * 6)'

    def testCalulator(self):
        self.assertEqual(MyCalc(self.exp1), eval(self.exp1))
        self.assertEqual(MyCalc(self.exp2), eval(self.exp2))
        self.assertEqual(MyCalc(self.exp3), eval(self.exp3))
        self.assertEqual(MyCalc(self.exp4), eval(self.exp4))
        self.assertEqual(MyCalc(self.exp5), eval(self.exp5))
        self.assertEqual(MyCalc(self.exp6), eval(self.exp6))


if __name__ == '__main__':
    unittest.main()
