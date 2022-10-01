from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        f = [[1_000_000_000 for j in range(n)] for i in range(m)]
        f[0][0] = grid[0][0]

        for j in range(1, n):
            f[0][j] = f[0][j - 1] + grid[0][j]
        for i in range(1, m):
            f[i][0] = f[i - 1][0] + grid[i][0]        
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
        return f[-1][-1]