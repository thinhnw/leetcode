from typing import List
class Solution:
    def time_needed(self, head) -> int:
        res = self.informTime[head]
        for i in self.children[head]:
            res += self.time_needed(i)
        return res
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.children = [[] for _ in range(n)]
        self.informTime = informTime
        for i in range(n):
            if manager[i] != -1:
                self.children[manager[i]].append(i)
        return self.time_needed(headID)

print(Solution().numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
