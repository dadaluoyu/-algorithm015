#lc_26_移动重复项

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        l = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[l] = nums[i]
                l += 1
        return l