class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashing = {}
        for i in range(0, len(nums)):
             
            hashing[nums[i]] = hashing.get(nums[i], 0) + 1 
             


        asc = sorted(hashing.items(), key=lambda item: item[1], reverse = True)[:k]
        result = []
        for i in asc:
            result.append(i[0])
        return result


        

        