class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)