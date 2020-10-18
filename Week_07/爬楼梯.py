#爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * 2
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            
            dp[i % 2] = dp[(i - 1) % 2] + dp[(i - 2) % 2]

        return dp[(n - 1) % 2]
