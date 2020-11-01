# LC 153 寻找旋转排序数组最小值

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if not nums:
            return []
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[0] <= nums[mid]:
                left = mid + 1          
            elif nums[mid - 1] >= nums[mid]:
                return nums[mid]
            else:    
                right = mid - 1
                
        return nums[0]