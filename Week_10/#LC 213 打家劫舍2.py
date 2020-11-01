#LC 213 打家劫舍2

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        pre1 = now1 = 0
        for i in nums[1:]: 
            pre1, now1 = now1, max(now1, pre1 + i)
        
        pre2 = now2 = 0
        for i in nums[:-1]: 
            pre2, now2 = now2, max(now2, pre2 + i)
        
        return max(now1, now2)