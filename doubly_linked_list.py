from typing import Any, Union


class Node(object):
    def __init__(self, value: Any, predecessor: Union['Node', type(None)],  successor: Union['Node', type(None)]):
        self.value = value
        self.prev = predecessor
        self.next = successor


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.__last_idx_c = -1

    def __str__(self):
        _repr = ''
        this = self.head
        while this:
            _repr += f'{this.value} <-> '
            this = this.next
        return _repr.rstrip(' <-> ')

    def append(self, value: Any):
        new_node = Node(value, None, None)
        if self.tail:
            tail = self.tail
            self.tail = new_node
            tail.next = self.tail
            self.tail.prev = tail
            return
        this = self.head
        if this is None:
            self.insert_at_beginning(value)
            return
        while this.next:
            this = this.next
        this.next = new_node
        self.tail = new_node
        self.tail.prev = this

    def insert_at_beginning(self, value: Any):
        head = Node(value, None, None)
        if self.head:
            head.next = self.head
            head.next.prev = head
        self.head = head

    def insert_at_end(self, value: Any):
        self.insert_after(value, self.tail)

    def insert_after(self, value: Any, after: 'Node'):
        new_node = Node(value, after, after.next)
        tail = new_node
        if after != self.tail:
            tail = None
            after.next.prev = new_node
        after.next = new_node
        self.tail = tail or self.tail

    def insert_before(self, value: Any, before: 'Node'):
        if before == self.head:
            self.insert_at_beginning(value)
        else:
            new_node = Node(value, before.prev, before)
            before.prev.next = new_node
            before.prev = new_node

    def insert(self, value: Any, after: 'Node' = None, before: 'Node' = None):
        if not (after or before):
            self.insert_at_beginning(value)
        elif not after:
            self.insert_after(value, after)
        else:
            self.insert_before(value, before)

    def remove(self, value: Any):
        this = self.head
        while this.next:
            if this.value == value:
                if this.prev:
                    this.prev.next = this.next
                else:
                    self.head = this.next
                this.next.prev = this.prev
                return
            this = this.next
        if value == this.value:
            self.tail = this.prev
            self.tail.next = None


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    print(dll)
    print('inserting 0 at beginning')
    dll.insert(0)
    print(dll)
    print('inserting 6 at end')
    dll.append(6)
    print(dll)
    print('removing 3')
    dll.remove(3)
    print(dll)
    print('removing 6')
    dll.remove(6)
    print(dll)
    print('removing 5')
    dll.remove(5)
    print(dll)
    print('appending 8')
    dll.insert_at_end(8)
    print(dll)
    print('insert 1 at beginning')
    dll.insert_at_beginning(1)
    print(dll)
    print('delete 0 & 1')
    dll.remove(0)
    dll.remove(1)
    print(dll)
    print(f'head: {dll.head.value}')
    print(f'tail: {dll.tail.value}')
