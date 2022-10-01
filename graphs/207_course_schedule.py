from typing import List
# class Solution:
#     def dfs(self, v):
#         self.color[v] = 1
#         for u in self.adj[v]:
#             if not self.color[u]:
#                 self.dfs(u)
#             elif self.color[u] == 1:
#                 self.res = False
#                 return 
#         self.color[v] = 2

#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         self.adj = [[] for _ in range(numCourses)]
#         for edge in prerequisites:
#             self.adj[edge[1]].append(edge[0])

#         self.color = [0 for _ in range(numCourses)] 

#         self.res = True
#         for v in range(numCourses):
#             if not self.color[v] and self.dfs(v):
#                 return self.res
#         return self.res

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        indegree = [0 for _ in range(numCourses)]        
        adj = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            indegree[edge[0]] += 1
            adj[edge[1]].append(edge[0])
        
        visited = [ i for i in range(numCourses) if not indegree[i] ]
        current_index = 0
        while current_index < len(visited):
            v = visited[current_index]
            if indegree[v] != 0:
                return False
            for u in adj[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    visited.append(u)
            current_index += 1
        return True
            
print(Solution().canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
        
        