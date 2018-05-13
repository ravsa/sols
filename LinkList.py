#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    data = None
    next_node = None


class NodeDoesNotExistError(Exception):

    def __init__(self, message="Node does not exist"):
        self.message = message
        super().__init__(self.message)


class EmptyLinkedListError(Exception):

    def __init__(self, message="LinkedList is empty"):
        self.message = message
        super().__init__(self.message)


class LinkedList:

    def __init__(self):
        self.root = None
        self.head = None

    def _insert(self, data):
        temp_node = Node()
        temp_node.data = data
        if not self.root:
            self.root = temp_node
        else:
            self.head.next_node = temp_node
        self.head = temp_node

    def insert(self, data):
        if isinstance(data, (list, tuple)):
            for i in data:
                self._insert(i)
        else:
            self._insert(data)

    def __iter__(self):
        current = self.root
        while current:
            yield current.data
            current = current.next_node

    def __len__(self):
        return len(list(self.__iter__()))

    def get_nodes(self):
        current = self.root
        while current:
            yield current
            current = current.next_node

    def get_node(self, num):
        for index, node in enumerate(self.get_nodes(), 1):
            if index == num:
                return node
        raise NodeDoesNotExistError("Node `{}` does not exist".format(num))

    def delete(self, num):
        if self.root:
            if num == 1:
                _temp = self.root
                self.root = self.root.next_node
                if self.root == self.head.next_node:
                    self.head = self.root
                del _temp
            else:
                _temp_cur = self.get_node(num)
                _temp_prev = self.get_node(num - 1)
                _temp_prev.next_node = _temp_cur.next_node
                del _temp_cur
        else:
            raise EmptyLinkedListError


a = LinkedList()
a.insert(1)
a.insert(2)
a.insert([3, 4, 5])
a.delete(5)
print(list(a))
