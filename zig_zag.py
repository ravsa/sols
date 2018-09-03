#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def skip(n):
    if n <= 1:
        return n - 1
    else:
        return n + (n-3)


inp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
out = ''
row = 5

for idx in range(row):
    k = skip(row - idx) + 1
    l = skip(idx) + 1
    temp_a = inp[idx:k]
    temp_b = inp[idx:l]
    _min = min(len(temp_a), len(temp_b))
    result = [None] * (_min*2)
    result[::2] = temp_a[:_min]
    result[1::2] = temp_b[:_min]
    result.extend(temp_a[:_min])
    result.extend(temp_b[:_min])
    print(result)
