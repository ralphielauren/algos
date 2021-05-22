# QUICK FIND

#  0 1 2 3 4 5 6 7 8 9      connect (0,5) (5,8)
#  5 1 2 3 4 5 6 7 8 9
#  8 1 2 3 4 8 6 7 8 9


class QuickFind:

    def __init__(self, N):
        self.lst = list(range(N))

    def connected(self, p, q):
        return self.lst[p] == self.lst[q]

    def union(self, p, q):
        if not self.connected(p, q):

            pval = self.lst[p]
            qval = self.lst[q]

            for index, value in enumerate(self.lst):
                if value == pval:
                    self.lst[index] = qval


if __name__ == "__main__":
    test = QuickFind(10)
    test.union(0, 5)
    print(test.lst)
    test.union(5, 0)
    print(test.lst)
    test.union(8, 5)
    print(test.lst)

