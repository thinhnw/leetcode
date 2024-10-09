from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.rows = [True for _ in range(n)]
        self.cols = [True for _ in range(n)]
        self.diag = [True for _ in range(2 * n - 1)]
        self.anti_diag = [True for _ in range(2 * n - 1)]
        self.output = []

        def backtrack(i, j, board):

            if j == n:
                if not self.rows[i]:
                    backtrack(i + 1, 0, board)
                return

            if i == n:
                self.output += [["".join(x) for x in board]]
                return

            #When board[i][j] == '.'
            backtrack(i, j + 1, board)

            #When board[i][j] == 'Q'
            if self.rows[i] and self.cols[j] and self.diag[i + j] and self.anti_diag[j - i]:
                self.rows[i] = False
                self.cols[j] = False
                self.diag[i + j] = False
                self.anti_diag[j - i] = False
                board[i][j] = 'Q'
                backtrack(i, j + 1, board)
                board[i][j] = '.'
                self.rows[i] = True
                self.cols[j] = True
                self.diag[i + j] = True
                self.anti_diag[j - i] = True    

        board = [['.' for _ in range(n)] for _ in range(n)] 
        backtrack(0, 0, board)
        return self.output

print(Solution().solveNQueens(4))