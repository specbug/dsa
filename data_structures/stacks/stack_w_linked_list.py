from typing import Any
from data_structures.linked_lists.singly_linked_list import LinkedList


class Stack(object):
    def __init__(self):
        self.__stack = LinkedList()
        self.__ptop = -1

    def __repr__(self):
        return self.__stack.__repr__()

    def push(self, value: Any):
        self.__stack.insert_at_beginning(value)
        self.__ptop += 1

    def pop(self):
        self.__ptop -= 1
        top = self.__stack.peek_first()
        self.__stack.remove_from_beginning()
        return top

    def peek(self):
        if self.size() > 0:
            return self.__stack.peek_first()

    def empty(self):
        return self.size() == 0

    def size(self):
        return self.__ptop + 1


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    print('popped:', stack.pop())
    print(stack)
    print('pushing 6')
    stack.push(6)
    print(stack)
    print('peeking:', stack.peek())
    print('emptying stack')
    while not stack.empty():
        print('popped:', stack.pop())
    print(f'stack size: {stack.size()}')
