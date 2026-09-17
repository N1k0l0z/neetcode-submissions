class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        hashing = {}

        n = len(nums)
        res = [1] * n

        acc = 1
        for j in range(n):
            res[j] = 1
            res[j] *= acc
            acc *= nums[j]

        acc = 1
        for j in range(n-1,-1,-1):
            res[j] *= acc
            acc *= nums[j]

        

        return res
        