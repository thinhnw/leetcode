from typing import List
class Solution:
    def backtrack(self, i):
        if i == len(self.rows):
            self.res.append(self.format(self.rows))
            return
        
        for j in range(len(self.rows)):
            if self.cols[j] and self.main_diag[j - i] and self.anti_diag[i + j]:
                self.cols[j] = False
                self.main_diag[j - i] = False
                self.anti_diag[i + j] = False
                self.rows[i] = j
                self.backtrack(i + 1)
                self.cols[j] = True
                self.main_diag[j - i] = True
                self.anti_diag[i + j] = True
        self.rows[i] = -1
    def format(self, rows):
        res = []
        for i in range(len(rows)):
            res.append([])
            for j in range(len(rows)):
                res[i].append(".")
            res[i][rows[i]] = "Q"
            res[i] = "".join(res[i])
        return res
    def totalNQueens(self, n: int) -> int:
        self.cols = [True for _ in range(n)]
        self.main_diag = [True for _ in range(n << 1)]
        self.anti_diag = [True for _ in range(n << 1)]
        self.rows = [-1 for _ in range(n)]
        self.res = []
        self.backtrack(0) 
        return len(self.res)