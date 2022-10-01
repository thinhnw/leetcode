from typing import List
class Solution:
    def maximumMinutes(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fired = [[-1 for j in range(n)] for j in range(m)]
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j, 0])
                    # print(i, j)
                    fired[i][j] = 0

        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]        
        while len(queue):
            u, v, steps = queue.pop(0)
            for k in range(4):
                u2 = u + di[k]
                v2 = v + dj[k]
                if u2 >= 0 and v2 >= 0 and v2 < n and u2 < m and grid[u2][v2] == 0 and fired[u2][v2] == -1:          
                    queue.append([u2, v2, steps + 1])
                    fired[u2][v2] = steps + 1

        l = 0
        r = 1_000_000_000
        while l <= r:
            minutes = (l + r) >> 1
            queue = [[0, 0, minutes]]
            visited = [[False for j in range(n)] for j in range(m)]
            visited[0][0] = True
            while len(queue):
                u, v, steps = queue.pop(0)
                for k in range(4):
                    u2 = u + di[k]
                    v2 = v + dj[k]
                    if u2 < 0 or v2 < 0 or v2 >= n or u2 >= m or grid[u2][v2]:
                        continue
                    is_before_fired = True if fired[u2][v2] == -1 else (steps < fired[u2][v2] if u2 == m - 1 and v2 == n - 1 else steps + 1 < fired[u2][v2])
                    # print(u2, v2)
                    if is_before_fired and not visited[u2][v2]:
                        queue.append([u2, v2, steps + 1])
                        visited[u2][v2] = True
            # print(minutes)
            # for i in range(m):
            #     print(visited[i])
            if visited[m - 1][n - 1]:
                l = minutes + 1
            else:
                r = minutes - 1

        # for i in range(m):
        #     print(fired[i])
        return l - 1

grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]] 
grid = [[0,0,0],[2,2,0],[1,2,0]]
grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
grid = [[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]]
print(Solution().maximumMinutes(grid))  
        