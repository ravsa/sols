#!/usr/bin/env python
# -*- coding: utf-8 -*-

__desc__ = "https://www.codechef.com/problems/RRPLAYER"

#  import sys
#  sys.stdin = open("input.txt")  # TestCases

for _ in xrange(int(raw_input())):
    N = float(raw_input())
    print(sum([N/j for j in range(1, int(N + 1))]))
