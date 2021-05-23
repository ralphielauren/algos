"""
DYNAMIC CONNECTIVITY - QUICK FIND
--------------------
Problem Statement:

Given a huge number of connected components in a sub-set,
how do we design an efficient data structure that allows
us to connect huge amounts of items together (our union method)
and efficiently determine if items are connected (our find method) ?
"""

#  Solution: QuickFind
#  0 1 2 3 4 5 6 7 8 9      union (0,5)
#  5 1 2 3 4 5 6 7 8 9      union (5,8)
#  8 1 2 3 4 8 6 7 8 9      union (7,8)


class QuickFind:
    def __init__(self, N):
        self.lst = list(range(N))

    def find(self, p, q):
        return self.lst[p] == self.lst[q]

    def union(self, p, q):
        if not self.find(p, q):

            p_val = self.lst[p]
            q_val = self.lst[q]

            for index, value in enumerate(self.lst):
                if value == p_val:
                    self.lst[index] = q_val


if __name__ == "__main__":
    test = QuickFind(10)
    test.union(0, 5)
    assert test.lst == [5, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    test.union(5, 0)
    assert test.lst == [5, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    test.union(5, 8)
    assert test.lst == [8, 1, 2, 3, 4, 8, 6, 7, 8, 9]
    test.union(7, 8)
    assert test.lst == [8, 1, 2, 3, 4, 8, 6, 8, 8, 9]
