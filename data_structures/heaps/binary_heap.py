from typing import Any
from data_structures.arrays.dynamic_arrays import Array


class BinaryHeap(object):
    def __init__(self):
        self._heap = Array()
        self._size = 0

    def __repr__(self):
        return self.display()

    def push(self, value: Any):
        self._heap.append(value)
        self._size += 1
        ptr = self.size() - 1
        self._bubble_up(ptr)

    def pop(self):
        self._swap(0, self.size() - 1)
        first = self._heap.pop()
        self._size -= 1
        self._bubble_down(0)
        return first

    def size(self):
        return self._size

    def peek(self):
        if self.size() > 0:
            return self._heap[0]

    def display(self):
        _repr = ''
        for i in range(0, self.size() // 2):
            _repr += (" PARENT : " + str(self._heap[i]) + " LEFT CHILD : " +
                      str(self._heap[2 * i + 1]) + " RIGHT CHILD : " +
                      str(self._heap[2 * i + 2]))
            _repr += "\n"
        return _repr

    @staticmethod
    def _parent(pos: int):
        return (pos-1)//2

    @staticmethod
    def _left_child(pos: int):
        return 2 * pos + 1

    @staticmethod
    def _right_child(pos: int):
        return 2 * pos + 2

    def _bubble_up(self, pos: int):
        raise NotImplementedError

    def _bubble_down(self, pos: int):
        raise NotImplementedError

    def _swap(self, pos1: int, pos2: int):
        self._heap[pos1], self._heap[pos2] = self._heap[pos2], self._heap[pos1]
