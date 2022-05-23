from typing import Any
from data_structures.heaps.binary_min_heap import MinBinaryHeap


class PriorityQueue(object):
    def __init__(self):
        self.__queue = MinBinaryHeap()
        self.__ptop = -1

    def __repr__(self):
        return self.__queue.__repr__()

    def enqueue(self, value: Any):
        self.__queue.push(value)
        self.__ptop += 1

    def dequeue(self):
        self.__ptop -= 1
        return self.__queue.pop()

    def peek(self):
        if self.size() > 0:
            return self.__queue.peek()

    def size(self):
        return self.__ptop + 1

    def empty(self):
        return self.size() == 0

    def __len__(self):
        return self.size()


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(8)
    pq.enqueue(3)
    pq.enqueue(1)
    pq.enqueue(5)
    pq.enqueue(7)
    pq.enqueue(6)
    pq.enqueue(4)
    pq.enqueue(2)
    print(pq)
    print('dequeue:', pq.dequeue())
    print(pq)
    print('emptying queue:')
    while not pq.empty():
        print(pq.dequeue())
    print('size:', pq.size())
