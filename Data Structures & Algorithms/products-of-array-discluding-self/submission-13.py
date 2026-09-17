class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        hashing = {}

        acc = 1
        for j, i in enumerate(nums):
            hashing[j] = hashing.get(j, 1) * acc
            acc *= i

        acc = 1
        for j, i in enumerate(nums[::-1]):
            hashing[len(nums)-j-1] = hashing.get(len(nums)-j-1, 1) * acc
            acc *= i

        return list(hashing.values())





        