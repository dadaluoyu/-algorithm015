#lc_55_跳跃游戏

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None:
            return False
        
        maxPos = len(nums) - 1
        for i in range(maxPos, -1, -1):
            if nums[i] + i >= maxPos:
                maxPos = i
        return maxPos == 0