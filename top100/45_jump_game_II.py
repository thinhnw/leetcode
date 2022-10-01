from typing import List
class Solution:
    def jump(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [-1 for _ in range(n)]
        f[0] = 0
        longest = 0
        for i in range(n):
            # print(i, f[i])
            if f[i] == -1:
                continue
            if i + nums[i] > longest:
                for j in range(longest + 1, min(n, i + nums[i] + 1)):
                    f[j] = f[i] + 1
                longest = i + nums[i]
        return f[-1]

print(Solution().jump([2,3,1,1,4])) 