from typing import Any


class DynamicArray(object):
    def __init__(self, n: int = 10):
        self.__init_size = n
        self.__array = [None] * n
        self.__last_idx_c = 0

    def append(self, value: Any):
        if self.__is_array_full():
            self.__resize()
        self.__last_idx_c += 1
        self.__setitem__(self.__last_idx_c, value)

    def clear(self):
        self.__array = []
        self.__last_idx_c = 0

    def copy(self):
        return self.__array[:]

    def count(self):
        return self.__init_size

    def extend(self):
        pass

    def index(self, value: Any):
        for i, v in enumerate(self.__array):
            if v == value:
                return i
        raise ValueError(f'{value} is not in array.')

    def insert(self, index: int, value: Any):
        if self.__is_array_full():
            self.__resize()
        array_new = self.__array[:index] + [value] + self.__array[index:]
        self.__array = array_new[:]
        self.__last_idx_c += 1

    def pop(self):
        pass

    def remove_at(self, index: int):
        array_new = self.__array[:index]
        if index < (self.count() - 1):
            array_new += self.__array[index+1:]
        self.__array = array_new[:]
        self.__last_idx_c -= 1

    def remove(self, value: Any, occurrence: int = 1):
        idx = None
        freq = 0
        for i, v in enumerate(self.__array):
            if v == value:
                freq += 1
                if freq == occurrence:
                    idx = i
                    break
        if not idx:
            raise IndexError(f'Value {value} not found for {occurrence} occurrence(s).')
        self.remove_at(idx)

    def reverse(self):
        return self.__array[::-1]

    def len(self):
        return self.__last_idx_c

    def __resize(self):
        print(f'Resizing array from {self.count()} to {self.count() * 2} elements.')
        array_new = self.__array + [None] * self.__init_size
        self.__array = array_new[:]
        self.__init_size *= 2

    def __is_array_full(self):
        return self.__array[-1] is not None

    def __len__(self):
        return self.len()

    def __repr__(self):
        return f'{self.__array[:self.__last_idx_c + 1]}'

    def __getitem__(self, index: int) -> Any:
        return self.__array[index]

    def __setitem__(self, index: int, value: Any):
        self.__array[index] = value
        self.__last_idx_c = max(index, self.__last_idx_c)

    def __delitem__(self, index: int):
        self.remove_at(index)


if __name__ == '__main__':
    arr = DynamicArray(n=5)
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    arr[3] = 4
    arr[4] = 5
    print(f'array: {arr}')
    print('appending 6')
    arr.append(6)
    print(arr)
    print(f'inserting 7 at index 6')
    arr.insert(6, 7)
    print(arr)
    print(f'setting index 7 to 9')
    arr[7] = 9
    print(arr)
    print(f'setting index 7 to 10')
    arr[7] = 10
    print(arr)
    print(f'removing value 10')
    arr.remove(10)
    print(arr)
    print(f'appending 8')
    arr.append(8)
    print(arr)
    print(f'Value at index 5: {arr[5]}')
    print(f'appending 9')
    arr.append(9)
    print(arr)
    print(f'appending 10')
    arr.append(10)
    print(arr)
    print(f'appending 11')
    arr.append(11)
    print(arr)
    print(f'appending 12')
    arr.append(12)
    print(arr)
    print(f'removing value at index 10')
    arr.remove_at(10)
    print(arr)
    print(f'index of 12:', arr.index(12))
    print(f'index of 11:')
    try:
        arr.index(11)
    except ValueError as exc:
        print(repr(exc))
    print(f'len of array: {len(arr)}')
