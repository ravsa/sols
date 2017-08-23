#!/usr/bin/env python
# -*- coding: utf-8 -*-

__desc__ = 'https://www.codechef.com/problems/PROPOSAL'

#  import sys
#  sys.stdin = open("input.txt")  # TestCases

N = input()
numbers = [0] * N
string = raw_input().split()

for i in xrange(N):
    numbers[i] = int(string[i])

res = 0

# main logic

mult1 = [0] * (N ** 3)
mult2 = [0] * (N ** 2)
num1 = num2 = 0

# generate all mult1
for i in xrange(N):
    for j in xrange(N):
        for k in xrange(N):
            if numbers[i] != 0:
                mult1[num1] = numbers[i] * 100 + numbers[j] * 10 + numbers[k]
                num1 += 1


# generate all mult2
for i in xrange(N):
    for j in xrange(N):
        if numbers[i] != 0:
            mult2[num2] = numbers[i] * 10 + numbers[j]
            num2 += 1

#multiply and check
for i in xrange(num1):
    for j in xrange(num2):
        _flag = 1
        _result = mult1[i] * (mult2[j] % 10)
        _result_store = _result
        if _result < 1000:
            while(_result != 0):
                dig = _result % 10
                if dig not in numbers:
                    _flag = 0
                    break
                _result = _result / 10
            if _flag == 1:
                result_par2 = mult1[i] * (mult2[j] / 10)
                result_par2_copy = result_par2
                if result_par2 < 1000:
                    while(result_par2 != 0):
                        dig = result_par2 % 10
                        if dig not in numbers:
                            _flag = 0
                            break
                        result_par2 = result_par2 / 10
                    if _flag == 1:
                        result = _result_store + result_par2_copy * 10
                        result_copy = result
                        if result < 10000:
                            while(result != 0):
                                dig = result % 10
                                if dig not in numbers:
                                    _flag = 0
                                    break
                                result = result / 10
                            if _flag == 1:
                                res += 1

print res
