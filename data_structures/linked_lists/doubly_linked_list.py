from typing import Any, Union


class Node(object):
    def __init__(self, value: Any, predecessor: Union['Node', type(None)],  successor: Union['Node', type(None)]):
        self.value = value
        self.prev = predecessor
        self.next = successor


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.__last_idx_c = -1

    def __repr__(self):
        _repr = ''
        this = self.head
        while this:
            _repr += f'{this.value} <-> '
            this = this.next
        return _repr.rstrip(' <-> ')

    def peek_first(self):
        return self.head.value

    def peek_last(self):
        return self.tail.value

    def insert_at_beginning(self, value: Any):
        head = Node(value, None, None)
        if self.head:
            head.next = self.head
            self.head.prev = head
        self.head = head
        if not self.tail:
            self.tail = head

    def insert_at_end(self, value: Any):
        tail = Node(value, self.tail, None)
        if self.tail:
            self.tail.next = tail
        self.tail = tail
        if not self.head:
            self.head = tail

    def insert_after(self, value: Any, after: Any):
        new_node = Node(value, None, None)
        this = self.head
        while this.next:
            if this.value == after:
                new_node.next = this.next
                new_node.prev = this
                this.next.prev = new_node
                this.next = new_node
                return
            this = this.next
        self.insert_at_end(value)

    def insert_before(self, value: Any, before: Any):
        new_node = Node(value, None, None)
        this = self.head
        while this:
            if this.value == before:
                new_node.next = this
                new_node.prev = this.prev
                if this == self.head:
                    self.insert_at_beginning(value)
                    return
                this.prev.next = new_node
                this.prev = new_node
                return
            this = this.next

    def remove_from_beginning(self):
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None

    def remove_from_end(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def remove(self, value: Any):
        this = self.head
        while this:
            if value == this.value:
                if this == self.head:
                    self.remove_from_beginning()
                    return
                if this == self.tail:
                    self.remove_from_end()
                    return
                this.prev.next = this.next
                this.next.prev = this.prev
                return
            this = this.next


if __name__ == '__main__':
    dll = LinkedList()
    dll.insert_at_beginning(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    print(dll)
    print('inserting 0 at beginning')
    dll.insert_at_beginning(0)
    print(dll)
    print('inserting 6 at end')
    dll.insert_at_end(6)
    print(dll)
    print('removing 3')
    dll.remove(3)
    print(dll)
    print('removing 6')
    dll.remove(6)
    print(dll)
    print('inserting 8 after 4')
    dll.insert_after(8, 4)
    print(dll)
    print('inserting 8 before 4')
    dll.insert_before(8, 4)
    print(dll)
    print('removing 5 from end')
    dll.remove_from_end()
    print(dll)
    print('inserting 8 at end')
    dll.insert_at_end(8)
    print(dll)
    print('insert 1 at beginning')
    dll.insert_at_beginning(1)
    print(dll)
    print('delete 0')
    dll.remove(0)
    print(dll)
    print('removing 1 from beginning')
    dll.remove_from_beginning()
    print(dll)
    print('removing two 8s')
    dll.remove(8)
    dll.remove(8)
    print(dll)
    print(f'head: {dll.head.value}')
    print(f'tail: {dll.tail.value}')
