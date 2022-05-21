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

    def append(self, value: Any):
        new_node = Node(value, None)
        if self.tail:
            tail = self.tail
            self.tail = new_node
            tail.next = self.tail
            return
        this = self.head
        if this is None:
            self.head = new_node
            return
        while this.next:
            this = this.next
        this.next = new_node
        self.tail = new_node

    def insert_at_beginning(self, value: Any):
        head = Node(value, None)
        if self.head:
            head.next = self.head
        self.head = head

    def insert_at_end(self, value: Any):
        self.insert_after(value, self.tail)

    def insert_after(self, value: Any, after: 'Node'):
        tail = None
        new_node = Node(value, after.next)
        if after == self.tail:
            tail = new_node
        after.next = new_node
        self.tail = tail or self.tail

    def insert_before(self, value: Any, before: 'Node'):
        if before == self.head:
            self.insert_at_beginning(value)
        else:
            this = self.head
            new_node = Node(value, None)
            while this.next:
                prev = this
                this = this.next
                if this == before:
                    new_node.next = this
                    prev.next = new_node
                    break

    def insert(self, value: Any, after: 'Node' = None, before: 'Node' = None):
        if not (after or before):
            self.insert_at_beginning(value)
        elif not after:
            self.insert_after(value, after)
        else:
            self.insert_before(value, before)

    def remove(self, value: Any):
        prev = this = self.head
        while this.next:
            this = this.next
            if value == this.value:
                prev.next = this.next
                if this == self.tail:
                    self.tail = prev
                break
            prev = this


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    print(sll)
    print('inserting 0 at beginning')
    sll.insert(0)
    print(sll)
    print('inserting 6 at end')
    sll.append(6)
    print(sll)
    print('removing 3')
    sll.remove(3)
    print(sll)
    print('removing 6')
    sll.remove(6)
    print(sll)
    print('removing 5')
    sll.remove(5)
    print(sll)
    print('appending 8')
    sll.insert_at_end(8)
    print(sll)
    print('insert 1 at beginning')
    sll.insert_at_beginning(1)
    print(sll)
    print('delete 0 & 1')
    sll.remove(0)
    sll.remove(1)
    print(sll)
    print(f'head: {sll.head.value}')
    print(f'tail: {sll.tail.value}')
