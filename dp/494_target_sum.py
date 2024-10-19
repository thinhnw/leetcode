class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target_limit = sum(nums) + abs(target)
        sum_ways = [[-1 for _ in range(target_limit * 2 + 1)] for _ in range(n)]
        def get_sum_ways(i: int, t: int) -> int:
            if i == -1:
                return t == 0
            if sum_ways[i][t] != -1:
                return sum_ways[i][t]
            sum_ways[i][t] = get_sum_ways(i-1, t+nums[i]) + get_sum_ways(i-1, t-nums[i])
            return sum_ways[i][t]
        return get_sum_ways(n-1, target)

        
        