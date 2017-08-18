#!/usr/bin/env python
# -*- coding: utf-8 -*-

__desc__ = 'https://www.codechef.com/problems/CARDS777'

#  import sys
#  sys.stdin = open("input.txt")  # TestCases

for _ in xrange(input()):
    R, B, P = map(int, raw_input().split())
    print(P * (R * 1.0 / (R + B)) + (R + B - P) * (B * 1.0 / (R + B)))
