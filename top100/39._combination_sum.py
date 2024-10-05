from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.output = []
        def backtrack(idx, count, candidates, target):
            if target == 0:
                tmp = []
                for i in range(len(candidates)):
                    tmp += [candidates[i]] * count[i]
                self.output.append(tmp)
                return
            if idx >= len(candidates):
                return
            
            count[idx] = 0
            while target >= count[idx] * candidates[idx]:
                backtrack(idx + 1, count, candidates, target - count[idx] * candidates[idx])
                count[idx] += 1
            count[idx] = 0
        backtrack(0, [0 for _ in range(len(candidates))], candidates, target)
        return self.output




Solution().combinationSum([2,3,6,7], 7)