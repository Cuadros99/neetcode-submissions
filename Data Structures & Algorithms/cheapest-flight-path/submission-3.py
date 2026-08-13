class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adjacency_map = defaultdict(list)
        for start, end, price in flights:
            adjacency_map[start].append((price, end))

        heap = [(0, -1, src)]        # cum_price, stops, airport
        best_stops = {}              # airport -> fewest stops it's been settled with

        while heap:
            cum_price, stops, airport = heapq.heappop(heap)

            if airport == dst:
                return cum_price
            if stops == k:
                continue
            if airport in best_stops and best_stops[airport] <= stops:
                continue
            best_stops[airport] = stops

            for price, neigh_ap in adjacency_map[airport]:
                heapq.heappush(heap, (cum_price + price, stops + 1, neigh_ap))

        return -1