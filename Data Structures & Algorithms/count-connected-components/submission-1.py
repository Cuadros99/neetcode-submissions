class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = list(range(n))
        self.rank = [1]*n
        num_partitions = n

        for l, r in edges:
            num_partitions -= self.union(l,r)

        return num_partitions


    def find(self, n):
        if  self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a, b):
        a_par = self.find(a)
        b_par = self.find(b)
        if a_par == b_par:
            return 0
        if self.rank[a_par] > self.rank[b_par]:
            self.parent[b_par] = a_par
        if self.rank[b_par] > self.rank[a_par]:
            self.parent[a_par] = b_par
        else:
            self.parent[b_par] = a_par
            self.rank[b_par] += 1

        return 1



