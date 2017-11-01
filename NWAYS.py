#!/usr/bin/env python
# -*- coding: utf-8 -*-

__desc__ = "https://www.codechef.com/problems/NWAYS"

#  import sys
#  sys.stdin = open("input.txt")  # TestCases

MOD, F = pow(10, 9) + 7, [1] * (pow(10, 7) + 5)

for i in xrange(2, 10**7 + 5):
    F[i] = i * F[i - 1] % MOD
for _ in xrange(input()):
    N, K = map(int, raw_input().split())
    ans = N + (2 * N * ((K + N + 1) * F[K + N] - (K + 2) * F[K + 1] * F[N]) * pow(
        (K + 1) * (K + 2) * F[K] * F[N], MOD - 2, MOD)) % MOD

    print(ans)
