class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airport_map = defaultdict(list)
        intinerary = []
        
        tickets.sort()
        for route in tickets:
            origin, dest = route
            airport_map[origin].append(dest)
        

        def dfs(airport):
            intinerary.append(airport)
            if len(intinerary) == (len(tickets)+1):
                return True
            
            for i, dest in enumerate(list(airport_map[airport])):
                airport_map[airport].pop(i)
                if dfs(dest): return True
                airport_map[airport].insert(i, dest)
            intinerary.pop()

            return False

        dfs("JFK")

        return intinerary
