"""
DYNAMIC CONNECTIVITY - QUICK UNION
--------------------
Problem Statement:

Given a huge number of connected components in a sub-set,
how do we design an efficient data structure that allows
us to connect huge amounts of items together (our union method)
and efficiently determine if items are connected (our find method) ?
"""

#  Solution: QuickUnion
#  - root = pointer to itself
#  - take root of component containing 1st item
#  and make that a child of the root of component of 2nd item
#  [   root of component of second item ==
#      parent of root of component of first item
#   ]
#  0 1 2 3 4 5 6 7 8 9      union (4,3)
#  0 1 2 3 3 5 6 7 8 9      union (3,8)
#  0 1 2 8 3 5 6 7 8 9      union (6,5)
#  0 1 2 8 3 5 5 7 8 9      union (9,4)
#  0 1 2 8 3 5 5 7 8 8      union (9,4)
#  0 1 1 8 3 5 5 7 8 8      union (2,1)
#  0 1 1 8 3 0 5 7 8 8      union (5,0)
#  0 1 1 8 3 0 5 1 8 8      union (7,2)
#  1 1 1 8 3 0 5 1 8 8      union (6,1)
#  1 8 1 8 3 0 5 1 8 8      union (7,3)


class QuickUnion:
    def __init__(self, n):
        # Array access: N
        self.parent_id = list(range(n))

    def __root(self, i):
        # root = pointer to itself
        # Array access: depth of i
        while i != self.parent_id[i]:
            i = self.parent_id[i]
        return i

    def connected(self, p, q):
        # Array access: depth of p + q
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        # Array access = depth of p + q
        if not self.connected(p, q):
            p_root = self.__root(p)
            q_root = self.__root(q)
            self.parent_id[p_root] = q_root


if __name__ == "__main__":
    test = QuickUnion(10)
    assert test.parent_id == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    test.union(4, 3)
    assert test.parent_id == [0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
    test.union(3, 8)
    assert test.parent_id == [0, 1, 2, 8, 3, 5, 6, 7, 8, 9]
    test.union(6, 5)
    assert test.parent_id == [0, 1, 2, 8, 3, 5, 5, 7, 8, 9]
    test.union(9, 4)
    test.union(2, 1)
    test.union(5, 0)
    test.union(7, 2)
    test.union(6, 1)
    test.union(7, 3)
    assert test.parent_id == [1, 8, 1, 8, 3, 0, 5, 1, 8, 8]
