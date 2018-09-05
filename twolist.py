#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.stdin = open("input.txt")  # TestCases


#  Definition for singly-linked list.
class ListNode:
    """ListNode class."""

    def __init__(self, x):
        """Initializer."""
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = root = None
        while l1 and l2:
            _sum = carry + l1.val + l2.val
            carry = _sum // 10
            val = _sum % 10
            if not result:
                result = ListNode(val)
                root = result
            else:
                result.next = ListNode(val)
                result = result.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            _sum = carry + l1.val
            carry = _sum // 10
            val = _sum % 10
            if not result:
                result = ListNode(val)
                root = result
            else:
                result.next = ListNode(val)
                result = result.next
            l1 = l1.next
        while l2:
            _sum = carry + l2.val
            carry = _sum // 10
            val = _sum % 10
            if not result:
                result = ListNode(val)
                root = result
            else:
                result.next = ListNode(val)
                result = result.next
            l2 = l2.next
        if carry != 0:
            result.next = ListNode(carry)
        return root


def node2list(lst):
    result = list()
    while lst:
        result.append(lst.val)
        lst = lst.next
    return result


S = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l3 = S.addTwoNumbers(l1, l2)
print(node2list(l3))
