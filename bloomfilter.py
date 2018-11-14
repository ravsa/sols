#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class BloomFilter:

    def __init__(self, length, fp_prob):
        # False Positive Probablity
        self.fp_prob = fp_prob

        # calculate the size of hashtable (M)
        self.size = self.get_size(length, fp_prob)

        # number of hash functions to use (K)
        self.hash_count = self.num_hash_function(self.size, length)

        self.bit_array = [False] * self.size

    def __set_bit(self, position, bit):
        self.bit_array[position] = bit

    def __get_bit(self, position):
        return self.bit_array[position]

    def __get_hash(self, value, number):
        value = '{}##{}'.format(str(value), str(number))
        return abs(hash(value))

    def add(self, item):
        temp = list()
        for i in range(self.hash_count):
            bit_position = self.__get_hash(item, i) % self.size
            temp.append(bit_position)
            self.__set_bit(bit_position, True)
        print(temp)

    def check(self, item):
        for i in range(self.hash_count):
            digest = self.__get_hash(item, i) % self.size
            if self.__get_bit(digest) is False:
                return False
        return True

    @staticmethod
    def get_size(n, p):
        return round(-(n * math.log(p))/(math.log(2)**2))

    @staticmethod
    def num_hash_function(m, n):
        return round((m/n) * math.log(2))
