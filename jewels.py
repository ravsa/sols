#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        store = {}

        for idx in S:
            store[idx] = store.get(idx, 0)
            store[idx] += 1

        result = 0
        for idx in J:
            result += store.get(idx, 0)
        return result
