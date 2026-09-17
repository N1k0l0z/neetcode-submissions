class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n  # Pre-allocate output array in contiguous memory

        # Pass 1: Compute prefix products
        acc = 1
        for i in range(n):  # Runs N times
            res[i] = acc  # O(1) assignment
            acc *= nums[i]  # O(1) multiplication

        # Pass 2: Multiply by suffix products
        acc = 1
        for i in range(n - 1, -1, -1):  # Runs N times backward
            res[i] *= acc  # O(1) in-place multiplication
            acc *= nums[i]  # O(1) multiplication

        return res