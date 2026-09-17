class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashing = {} # val: freq

        for i in nums:
            hashing[i] = hashing.get(i, 0) + 1
        
        freqs = [[] for l in range(len(nums) + 1)]

        for l, j in hashing.items():
            freqs[j].append(l)

        result = []
        for i in freqs:
            if i != []:
                result.extend(i)

        return result[-k:]

        