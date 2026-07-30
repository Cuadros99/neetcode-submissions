class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = list(range(len(edges)))

        for left, right in edges:
            if not self.union(left-1, right-1):
                return [left, right]

    def find(self, n):
        if self.parent[n] != n:
            return self.find(self.parent[n])
        return n

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        else:
            self.parent[root_b] = root_a
            return True
        
#   O(E + alfa(V))