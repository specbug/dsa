from typing import Any
from data_structures.arrays.dynamic_arrays import Array


class DisjointSet(object):
    def __init__(self, elements: 'Array'):
        self._set = elements
        self._parent = dict()
        self._rank = Array.array([1] * len(elements))
        self.__init_parent__()

    def __repr__(self):
        return str(self._parent).strip('}').strip('{').replace(', ', '\n')

    def __init_parent__(self):
        for i, v in enumerate(self._set):
            self._parent[str(v)] = i

    def find(self, x: str):
        if self._set[self._parent[str(x)]] == x:
            return self._parent[str(x)]
        self._parent[x] = self.find(self._set[self._parent[str(x)]])
        return self._parent[x]

    def unify(self, m: str, n: str):
        m_set = self.find(m)
        n_set = self.find(n)
        if m_set == n_set:
            return
        if self._rank[m_set] > self._rank[n_set]:
            self._parent[self._set[n_set]] = m_set
            self._rank[m_set] += n_set
        else:
            self._parent[self._set[m_set]] = n_set
            self._rank[n_set] += m_set


if __name__ == '__main__':
    l = Array.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    dset = DisjointSet(l)
    dset.unify('a', 'b')
    dset.unify('c', 'd')
    dset.unify('e', 'f')
    dset.unify('g', 'h')
    dset.unify('i', 'j')
    dset.unify('a', 'c')
    dset.unify('b', 'd')
    dset.unify('e', 'g')
    dset.unify('f', 'h')
    dset.unify('i', 'j')
    print(dset)
    print(f'a and b are in the same set: {dset.find("a") == dset.find("b")}')
    print(f'c and e are in the same set: {dset.find("c") == dset.find("e")}')
    print(f'f and h are in the same set: {dset.find("f") == dset.find("h")}')
    print(f'a and j are in the same set: {dset.find("a") == dset.find("j")}')
