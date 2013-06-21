# -*- coding:utf-8 -*-
# 구구단 표를 세로로 출력하시오.

nth = ""
for i in range(1, 10):
    print " ".join([str(i * j) for j in range(2, 10)])
