from typing import Any
from data_structures.arrays.dynamic_arrays import Array


class Stack(object):
    def __init__(self):
        self.__stack = Array()
        self.__ptop = -1

    def __repr__(self):
        _repr = self.__stack.__repr__().strip('[').strip(']')
        return ' -> '.join(_repr.split(', ')[::-1])

    def push(self, value: Any):
        self.__stack.append(value)
        self.__ptop += 1

    def pop(self):
        self.__ptop -= 1
        return self.__stack.pop()

    def peek(self):
        if self.size() > 0:
            return self.__stack[self.__ptop]

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
