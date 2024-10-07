from typing import List

class Solution:    

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [a + 1 for a in range(amount + 1)]        
        dp[0] = 0                
        for a in range(amount + 1):
            if dp[a] == a + 1:
                continue
            for c in coins:
                if a + c <= amount:
                    dp[a + c] = min(dp[a + c], dp[a] + 1)
        if dp[amount] != amount + 1:
            return dp[amount]
        return -1