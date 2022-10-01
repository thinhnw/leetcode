from typing import List
class Solution:
    def dfs(self, v):
        self.color[v] = 1
        for u in self.adj[v]:
            if not self.color[u]:
                self.dfs(u)
            elif self.color[u] == 1:
                self.res = False
                return 
        self.color[v] = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            self.adj[edge[1]].append(edge[0])

        self.color = [0 for _ in range(numCourses)] 

        self.res = True
        for v in range(numCourses):
            if not self.color[v] and self.dfs(v):
                return self.res
        return self.res