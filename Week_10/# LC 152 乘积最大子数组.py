# LC 152 乘积最大子数组

class Solution:
    def maxProduct(self, nums: List[int]) -> int:  
        max0 = min0 = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0: max0, min0 = min0, max0
            max0 =  max(nums[i]*max0, nums[i])
            min0 =  min(nums[i]*min0, nums[i])
            res = max(res, max0)
        return res