#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HashMap:

    def __init__(self):
        self.size = 1
        self.map = [None] * self.size

    def get_hash(self, key):
        return sum([ord(ch) for ch in key]) % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
        else:
            for _key_value in self.map[key_hash]:
                if key == _key_value[0]:
                    _key_value[1] = value
                    break
            else:
                self.map[key_hash].append(key_value)
