class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjacency_map = defaultdict(list)

        for f in flights:
            start, end, price = f
            adjacency_map[start].append((price, end))

        heap = [(0, -1, src)]
        best_stops = {}

        while heap:
            print(heap)
            cum_price, stops, ap = heapq.heappop(heap)
            
            if ap == dst:
                return cum_price
            if stops == k:
                continue
            if ap in best_stops and best_stops[ap] <= stops:
                continue

            best_stops[ap] = stops

            for neighbor in adjacency_map[ap]:
                price, neigh_ap = neighbor
                heapq.heappush(
                    heap, 
                    (
                        cum_price + price,
                        stops+1,
                        neigh_ap
                    )
                )

        return -1

        
        
        
        
        
        
        
        
        #   [0, 5, 10]
        #   [5, 2, 10]
        #   src = 0
        #   dst = 2
        #   k = 2
        #   output = 20 (0 -> 5 -> 2)

        #   k = 0 
        #   output = -1 