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
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return 0
        if self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root
        if self.rank[b_root] > self.rank[a_root]:
            self.parent[a_root] = b_root
        else:
            self.parent[b_root] = a_root
            self.rank[b_root] += 1

        return 1



