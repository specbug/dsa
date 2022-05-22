from typing import Any, Union


class Node(object):
    def __init__(self, value: Any, successor: Union['Node', type(None)]):
        self.value = value
        self.next = successor


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.__last_idx_c = -1

    def __str__(self):
        _repr = ''
        this = self.head
        while this:
            _repr += f'{this.value} -> '
            this = this.next
        return _repr.rstrip(' -> ')

    def insert_at_beginning(self, value: Any):
        head = Node(value, None)
        if self.head:
            head.next = self.head
        self.head = head

    def insert_at_end(self, value: Any):
        new_node = Node(value, None)
        this = self.head
        while this.next:
            this = this.next
        this.next = new_node
        self.tail = new_node

    def insert_after(self, value: Any, after: Any):
        new_node = Node(value, None)
        this = self.head
        while this.next:
            if this.value == after:
                new_node.next = this.next
                this.next = new_node
                return
            this = this.next
        self.insert_at_end(value)

    def insert_before(self, value: Any, before: Any):
        new_node = Node(value, None)
        prev = None
        this = self.head
        while this.next:
            if this.value == before:
                if not prev:
                    self.insert_at_beginning(value)
                    return
                new_node.next = this
                prev.next = new_node
                return
            prev = this
            this = this.next

    def remove_from_beginning(self):
        self.head = self.head.next

    def remove_from_end(self):
        prev = None
        this = self.head
        while this.next:
            prev = this
            this = this.next
        self.tail = prev
        self.tail.next = None

    def remove(self, value: Any):
        prev = None
        this = self.head
        while this:
            if value == this.value:
                if not prev:
                    self.remove_from_beginning()
                    return
                prev.next = this.next
                if this == self.tail:
                    self.tail = prev
                return
            prev = this
            this = this.next


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.insert_at_beginning(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    print(sll)
    print('inserting 0 at beginning')
    sll.insert_at_beginning(0)
    print(sll)
    print('inserting 6 at end')
    sll.insert_at_end(6)
    print(sll)
    print('removing 3')
    sll.remove(3)
    print(sll)
    print('removing 6')
    sll.remove(6)
    print(sll)
    print('inserting 8 after 4')
    sll.insert_after(8, 4)
    print(sll)
    print('inserting 8 before 4')
    sll.insert_before(8, 4)
    print(sll)
    print('removing 5 from end')
    sll.remove_from_end()
    print(sll)
    print('inserting 8 at end')
    sll.insert_at_end(8)
    print(sll)
    print('insert 1 at beginning')
    sll.insert_at_beginning(1)
    print(sll)
    print('delete 0')
    sll.remove(0)
    print(sll)
    print('removing 1 from beginning')
    sll.remove_from_beginning()
    print(sll)
    print('removing two 8s')
    sll.remove(8)
    sll.remove(8)
    print(sll)
    print(f'head: {sll.head.value}')
    print(f'tail: {sll.tail.value}')
