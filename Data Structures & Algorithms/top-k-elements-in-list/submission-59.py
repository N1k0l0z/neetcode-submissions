class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashing = {}
        for i in range(0, len(nums)):
            hashing[nums[i]] = hashing.get(nums[i], 0) + 1 
            
        freqs = [[] for _ in range(0, len(nums) + 1)]

        for num, count in hashing.items():
            freqs[count].append(num)

        result = []
        for h in freqs[::-1]:
            for num in h:
                result.append(num)
                if len(result) == k:
                    return result
        return result