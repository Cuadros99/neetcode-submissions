class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(lambda: [[],[]])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key][0].append(timestamp)
        self.hashmap[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
            
        times_list = self.hashmap[key][0]
        n = len(times_list)
        i_prev_time=-1

        l, r = 0, n-1
        
        while l <= r:
            m = (l+r)//2
             
            if times_list[m] <= timestamp:
                i_prev_time = m
                l = m + 1
            elif times_list[m] > timestamp:
                r = m - 1
        if i_prev_time == -1:
            return ""
        else:
            return self.hashmap[key][1][i_prev_time]
