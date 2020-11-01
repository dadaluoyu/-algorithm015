# LC 53 最大子序和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return
        n = len(nums)
        dp = [0 for i in range(n)]
        maxSum = dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 1], nums[i])
            maxSum = max(dp[i], maxSum)
        return maxSum