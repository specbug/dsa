from data_structures.heaps.binary_heap import BinaryHeap


class MinBinaryHeap(BinaryHeap):
    def _bubble_up(self, pos: int):
        curr = self._heap[pos]
        pnt = self._heap[self._parent(pos)]
        while pnt and curr < pnt:
            self._swap(pos, self._parent(pos))
            pos = self._parent(pos)
            curr = self._heap[pos]
            pnt = self._heap[self._parent(pos)]

    def _bubble_down(self, pos: int):
        curr = self._heap[pos]
        if (2 * pos + 1) > self.size():
            return
        lft = self._heap[self._left_child(pos)]
        rgt = self._heap[self._right_child(pos)]
        while (rgt or lft) and (curr > lft if lft else False or curr > rgt if rgt else False):
            if lft and curr >= lft:
                self._swap(pos, self._left_child(pos))
                pos = self._left_child(pos)
            else:
                self._swap(pos, self._right_child(pos))
                pos = self._right_child(pos)
            if (2 * pos + 1) > self.size():
                return
            curr = self._heap[pos]
            lft = self._heap[self._left_child(pos)]
            rgt = self._heap[self._right_child(pos)]


if __name__ == '__main__':
    heap = MinBinaryHeap()
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
