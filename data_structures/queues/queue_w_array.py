from typing import Any
from data_structures.arrays.dynamic_arrays import Array


class Queue(object):
    def __init__(self):
        self.__queue = Array()
        self.__ptop = -1

    def __repr__(self):
        _repr = self.__queue.__repr__().strip('[').strip(']')
        return _repr.replace(', ', ' -> ')

    def enqueue(self, value: Any):
        self.__queue.append(value)
        self.__ptop += 1

    def dequeue(self):
        top = self.__queue[0]
        del self.__queue[0]
        self.__ptop -= 1
        return top

    def peek(self):
        if self.size() > 0:
            return self.__queue[0]

    def size(self):
        return self.__ptop + 1

    def empty(self):
        return self.size() == 0


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print('dequeue:', q.dequeue())
    print(q)
    print('dequeue:', q.dequeue())
    print(q)
    print('peek:', q.peek())
    print('enqueuing 6')
    q.enqueue(6)
    print(q)
    print('enqueuing 7')
    q.enqueue(7)
    print(q)
    print('emptying queue...')
    while q.size() > 0:
        print('dequeue:', q.dequeue())
    print('emptied queue')
    print('size:', q.size())
