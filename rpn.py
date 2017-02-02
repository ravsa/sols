#!/usr/bin/env python
# -*- coding: utf-8 -*-

# reverse polish notation python
import string


class RPN(object):

    """Reverse Polish Notaions"""

    def __init__(self, input_expr):
        self._input_expr = [_ for _ in input_expr if not _.isspace()]
        self._stack = list()
        self._output = list()
        self._prec = {
            '^': 4,
            '/': 3,
            '*': 3,
            '+': 2,
            '-': 2,
            '(': 1,
        }

    def rpn(self):
        for token in self._input_expr:
            if token in string.ascii_letters or token in string.digits:
                self._output.append(token)
            elif token == '(':
                self._stack.append(token)
            elif token == ')':
                tokenpop = self._stack.pop()
                while tokenpop != '(':
                    self._output.append(tokenpop)
                    tokenpop = self._stack.pop()
            else:
                while (len(self._stack) != 0) and (
                        self._prec[self._stack[-1]] >= self._prec[token]):
                    self._output = self._stack.pop()
                self._stack.append(token)
        return ''.join(self._output)

        


print "Hello,World!"
