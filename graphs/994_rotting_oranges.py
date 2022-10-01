from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for j in range(n)] for j in range(m)]
        a = grid
        ans = 0 
        queue = []

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and a[i][j] == 2:
                    queue.append([i, j, 0])
                    # print(i, j)
                    visited[i][j] = True

        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]        
        while len(queue):
            u, v, steps = queue.pop(0)
            for k in range(4):
                u2 = u + di[k]
                v2 = v + dj[k]
                if u2 >= 0 and v2 >= 0 and v2 < n and u2 < m and a[u2][v2] != 0 and not visited[u2][v2]:
                    ans = max(ans, steps + 1)
                    # print(u2, v2, steps + 1)
                    queue.append([u2, v2, steps + 1])
                    visited[u2][v2] = True

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and a[i][j] == 1:
                    return -1
                    
        return ans
        
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  
        