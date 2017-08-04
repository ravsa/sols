#!/usr/bin/env python
# -*- coding: utf-8 -*-

__desc__ = "https://www.codechef.com/problems/TREEROOT"

#  import sys
#  sys.stdin = open("input.txt")  # TestCases

for _ in xrange(input()):
    sum1 = sum2 = 0
    for _ in xrange(input()):
        [x, y] = map(int, raw_input().split())
        sum1 += x
        sum2 += y
    print -sum2 + sum1
