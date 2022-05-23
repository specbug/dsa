from typing import Any
from data_structures.arrays.dynamic_arrays import Array


class MinHeap(object):
    def __init__(self):
        self.__heap = Array()
        self.__size = 0

    def __repr__(self):
        return self.display()

    def push(self, value: Any):
        self.__heap.append(value)
        self.__size += 1
        ptr = self.size() - 1
        self._bubble_up(ptr)

    def pop(self):
        self._swap(0, self.size() - 1)
        first = self.__heap.pop()
        self.__size -= 1
        self._bubble_down(0)
        return first

    def size(self):
        return self.__size

    def peek(self):
        if self.size() > 0:
            return self.__heap[0]

    def display(self):
        _repr = ''
        for i in range(0, self.size() // 2):
            _repr += (" PARENT : " + str(self.__heap[i]) + " LEFT CHILD : " +
                      str(self.__heap[2 * i + 1]) + " RIGHT CHILD : " +
                      str(self.__heap[2 * i + 2]))
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
        curr = self.__heap[pos]
        pnt = self.__heap[self._parent(pos)]
        while pnt and curr < pnt:
            self._swap(pos, self._parent(pos))
            pos = self._parent(pos)
            curr = self.__heap[pos]
            pnt = self.__heap[self._parent(pos)]

    def _bubble_down(self, pos: int):
        curr = self.__heap[pos]
        if (2 * pos + 1) > self.size():
            return
        lft = self.__heap[self._left_child(pos)]
        rgt = self.__heap[self._right_child(pos)]
        while rgt and lft and (curr > lft or curr > rgt):
            if curr > rgt:
                self._swap(pos, self._right_child(pos))
                pos = self._right_child(pos)
            else:
                self._swap(pos, self._left_child(pos))
                pos = self._left_child(pos)
            if (2 * pos + 1) > self.size():
                return
            curr = self.__heap[pos]
            lft = self.__heap[self._left_child(pos)]
            rgt = self.__heap[self._right_child(pos)]

    def _swap(self, pos1: int, pos2: int):
        self.__heap[pos1], self.__heap[pos2] = self.__heap[pos2], self.__heap[pos1]


if __name__ == '__main__':
    heap = MinHeap()
    heap.push(5)
    heap.push(3)
    heap.push(7)
    heap.push(2)
    heap.push(4)
    print(f'pop: {heap.pop()}')
    heap.push(6)
    heap.push(8)
    heap.push(1)
    heap.push(9)
    print(heap)
    while heap.size() > 0:
        print(f'Popped: {heap.pop()}')
