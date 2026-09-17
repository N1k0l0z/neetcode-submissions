class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        hashing = {}
        n = len(nums)
        acc = 1
        for j in range(n):
            hashing[j] = 1
            hashing[j] *= acc
            acc *= nums[j]

        acc = 1
        for j in range(n-1,-1,-1):
            hashing[j] *= acc
            acc *= nums[j]

        return list(hashing.values())





        