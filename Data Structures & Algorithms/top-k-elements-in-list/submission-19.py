class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums.sort()

        hashing = {}
        for i in range(0, len(nums)):
            if i != 0:
                if nums[i] in hashing:
                    if nums[i] == nums[i-1]:
                        if nums[i] in hashing:
                            hashing[nums[i]] += 1
                        else:
                            hashing[nums[i]] = 1
                else:
                    hashing[nums[i]] = 1
            else:
                hashing[nums[i]] = 1       
        asc = sorted(hashing.items(), key=lambda item: item[1], reverse = True)[:k]
        result = []
        for i in asc:
            result.append(i[0])
        return result


        

        