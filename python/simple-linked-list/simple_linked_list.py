"""Implement a simple linked list"""

# pylint: disable=missing-function-docstring,missing-class-docstring

class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        self._head = None

        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current.value()
            current = current.next()

    def __len__(self):
        return sum(1 for _node in self)

    def head(self):
        if self._head is None:
            raise EmptyListException('The list is empty.')
            
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)

    def pop(self):
        if self._head is None:
            raise EmptyListException('The list is empty.')

        value = self._head.value()
        self._head = self._head.next()
        return value

    def reversed(self):
        return LinkedList(self)
