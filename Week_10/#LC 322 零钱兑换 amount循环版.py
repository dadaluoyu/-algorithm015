#LC 322 零钱兑换 amount循环版

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(0, amount + 1):
            for coin in coins:
                if i - coin > 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    #print(dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1


