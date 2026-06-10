class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        bucket_sort = [ [] for i in range(len(nums) + 1) ]

        for n, f in counter.items():
            bucket_sort[f].append(n)

        k_most_freq = []
        for f in range(len(nums), 0, -1):
            for n in bucket_sort[f]:
                k_most_freq.append(n)
                if len(k_most_freq) == k:
                    return k_most_freq

        