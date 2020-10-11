#lc 33 分段二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left ) // 2
            if nums [mid] == target:
                return mid
            
            #只考虑mid在target左边的情况，剩下都是else
            if nums[0] <= nums[mid] and (nums[mid] < target or target < nums[0]): 
                #mid在左半段，且target同在左半段，条件是大于mid 或者 target在右半段 小于 nums[0]
                left = mid + 1
            elif target < nums[0] and target > nums[mid]:
                #target与mid同在右半段且target比mid大
                #最右边的单调 区间
                left = mid + 1
            else:
                right = mid - 1     
                
            
        return -1