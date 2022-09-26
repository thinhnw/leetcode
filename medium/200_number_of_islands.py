class Solution:
    def bfs(self, i, j):
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]        
        queue = [[i, j]]
        while len(queue):
            u, v = queue.pop(0)
            for k in range(4):
                u2 = u + di[k]
                v2 = v + dj[k]
                if u2 >= 0 and v2 >= 0 and v2 < self.n and u2 < self.m and self.a[u2][v2] == "1" and not self.visited[u2][v2]:
                    queue.append([u2, v2])
                    self.visited[u2][v2] = True
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = [[False for j in range(self.n)] for j in range(self.m)]
        self.a = grid
                
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and self.a[i][j] == "1":
                    self.bfs(i, j)
                    count += 1
                    
        return count
        
        
        