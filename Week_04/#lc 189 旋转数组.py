#lc 189 旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.rev(nums, 0, len(nums) - 1)
        self.rev(nums, 0, k - 1)
        self.rev(nums, k , len(nums) - 1)
        
    def rev(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums