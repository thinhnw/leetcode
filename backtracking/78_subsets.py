from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.subsets = []
        self.subset = []
        self.backtrack(0)
        return self.subsets


    def backtrack(self, i):
        if i == len(self.nums):
            self.subsets.append([_ for _ in self.subset])
            return
        self.backtrack(i + 1)
        self.subset.append(self.nums[i])
        print(self.subset)
        self.backtrack(i + 1)
        self.subset.pop()


print(Solution().subsets([1, 2, 3]))