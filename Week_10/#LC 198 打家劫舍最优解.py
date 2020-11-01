#LC 198 打家劫舍最优解
class Solution:
    def rob(self, nums: List[int]) -> int: 
        pre = now = 0
        for i in nums: 
            pre, now = now, max(now, pre + i)  
        return now