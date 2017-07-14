#!/usr/bin/env python
# -*- coding: utf-8 -*-

__url__ = 'https://www.codechef.com/problems/MRO'

from math import pow
#  import sys
#  sys.stdin = open("input.txt")  # TestCases

start, end = 4, int(pow(10, 5) + 2)
A = [0, 1, 1, 3]
series = [1, 2, 4, 8]
mod = int(pow(10, 9) + 7)

for index in range(start, int(end)):
    series.append((series[index - 1] * 2) % mod)
    A.append((A[index - 1] * (series[index - 1] - 1)) % mod)

for _ in range(int(raw_input())):
    print(int(A[int(raw_input())]))
