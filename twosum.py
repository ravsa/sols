#!/usr/bin/env python3
# -*- coding: utf-8 -*-


nums = [2, 7, 11, 12]
target = 9


def result(nums, target):
    dict = {}
    for i in range(len(nums)):
        _temp = target - nums[i]
        if _temp not in dict:
            dict[nums[i]] = i
        else:
            return [dict[_temp], i]


print(result(nums, target))
