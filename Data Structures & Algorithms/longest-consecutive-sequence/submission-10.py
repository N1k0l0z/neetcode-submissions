class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        hashing = {}

        n = 0
        for i in sorted(nums):
            if n not in hashing:
                hashing[n] = [i]
            elif hashing[n][-1] + 1 == i:
                hashing[n].append(i)
            elif hashing[n][-1] == i:
                continue
            else:
                n += 1
                hashing[n] = [i]
                
        highest_num = 0
        for i in hashing:
            if len(hashing.get(i)) > highest_num:
                highest_num = len(hashing.get(i))

       
        return highest_num