class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[-1][-1]