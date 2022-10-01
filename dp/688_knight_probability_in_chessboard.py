di = [-2, -2, -1, 1, 2, 2, 1, -1]
dj = [-1, 1, 2, 2, 1, -1, -2, -2]
class Solution:
    def calc(self, i, j, step) -> int:
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            return 0
        if step == 0:
            return self.f[i][j][0]
        # print(i, j)
        if self.f[i][j][step] != -1:
            return self.f[i][j][step]

        self.f[i][j][step] = 0        
        for x in range(8):
            i2 = i + di[x]
            j2 = j + dj[x]
            self.f[i][j][step] += self.calc(i2, j2, step - 1)
        # print(i, j, 'step =', step, 'res = ', self.f[i][j][step])
        return self.f[i][j][step]


    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.f = [[[-1 for i in range(k + 1)] for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                self.f[i][j][0] = 0
        self.f[row][column][0] = 1
        self.row = row
        self.column = column
        self.n = n

        on = 0
        for i in range(n):
            x = []
            for j in range(n):
                on += self.calc(i, j, k)
                x.append(self.calc(i, j, k))
            # print(x)
        # off = 0
        # for step in range(k):
        #     for i in range(n):
        #         for j in range(n):
        #             for z in range(8):
        #                 i2 = i + di[z]
        #                 j2 = j + dj[z]
        #                 if i2 < 0 or j2 < 0 or i2 >= n or j2 >= n:
        #                     off += self.f[i][j][step]
        #     print(step, off)
        # print(on, off)
        return on/(8**k)

print(Solution().knightProbability(3, 2, 0, 0))