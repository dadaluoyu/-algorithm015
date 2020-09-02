#leetcode_283 移动零

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                if l != r:
                    nums[l] = nums[r]
                l += 1
        while l < len(nums):
            nums[l] = 0
            l += 1
            
            