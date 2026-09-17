class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasz = 0

        for num in nums:
            if num != 0:
                product*=num
            else:
                hasz+=1
        if hasz > 1:
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if hasz:
                    nums[i] = 0
                else:
                    nums[i] = int(product / nums[i])
            else:
                nums[i] = product
        return nums