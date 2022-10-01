class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [False for _ in range(n)]
        f[0] = True
        longest = 0
        for i in range(0, n):
            if not f[i]:
                continue
            if i + nums[i] > longest:
                for j in range(longest + 1, min(n, i + nums[i] + 1)):
                    f[j] = True
                longest = i + nums[i]
        return f[-1]
            