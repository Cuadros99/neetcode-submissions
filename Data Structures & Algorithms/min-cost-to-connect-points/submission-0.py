class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        cost = 0
        edges_counter = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xa, ya = points[i]
                xb, yb = points[j]
                distance = abs(xa-xb) + abs(ya -yb)
                edge = (distance, (xa, ya), (xb, yb))
                edges.append(edge)

        heapq.heapify(edges)

        self.parents = {(x,y): (x,y) for x, y in points}
        self.rank = {(x,y): 0 for x, y in points}

        while edges and edges_counter < len(points) - 1:
            d, pa, pb = heapq.heappop(edges)
            if self.union(pa, pb):
                cost += d
                edges_counter += 1

        return cost

    
    def find(self, point):
        x, y = point
        if self.parents[(x,y)] != (x,y):
            self.parents[(x,y)] = self.find(self.parents[(x,y)])
        return self.parents[(x,y)]
    
    def union(self, pa, pb):
        root_a = self.find(pa)
        root_b = self.find(pb)
        if root_a == root_b:
            return False
        if self.rank[root_a] > self.rank[root_b]:
            self.parents[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.rank[root_a] += 1
        return True


    
