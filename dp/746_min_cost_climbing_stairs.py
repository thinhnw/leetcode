class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f = [1_000_000 for _ in cost]
        f[0] = 0
        f[1] = 0        
        for i in range(2, len(cost)):
            f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])
        return min(f[-1] + cost[-1], f[-2] + cost[-2])