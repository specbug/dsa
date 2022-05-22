from typing import Any
from data_structures.linked_lists.doubly_linked_list import LinkedList


class Queue(object):
    def __init__(self):
        self.__queue = LinkedList()
        self.__ptop = -1

    def __repr__(self):
        return self.__queue.__repr__().replace('<->', '->')

    def enqueue(self, value: Any):
        self.__queue.insert_at_end(value)
        self.__ptop += 1

    def dequeue(self):
        top = self.__queue.peek_first()
        self.__queue.remove_from_beginning()
        self.__ptop -= 1
        return top

    def peek(self):
        if self.size() > 0:
            return self.__queue.peek_first()

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
