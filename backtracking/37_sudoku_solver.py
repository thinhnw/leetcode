from typing import List
from math import floor
class Solution:
    def backtrack(self, i, j):
        if i == 9:
            self.ans_found = True
            for x in range(9):
                print(self.board[x])
            # for x in range(9):
            #     print(self.rows[x])
            return
        # if i == 0 and j == 7:
        #     print(self.board[i])
        #     print(self.rows[i])
        nexti = i
        nextj = j + 1        
        if nextj == 9:
            nextj = 0
            nexti = i + 1
        
        if self.board[i][j] != ".":
            self.backtrack(nexti, nextj)
        else:
            for c in range(1, 10):
                box_id = self.get_box_id(i, j)
                if self.rows[i][c] and self.cols[j][c] and self.boxes[box_id][c]:
                    self.rows[i][c] = False
                    self.cols[j][c] = False
                    self.boxes[box_id][c] = False
                    self.board[i][j] = chr(c + 48)
                    self.backtrack(nexti, nextj)
                    if self.ans_found:
                        return
                    self.rows[i][c] = True
                    self.cols[j][c] = True
                    self.boxes[box_id][c] = True
            self.board[i][j] = "."
    def get_box_id(self, i, j) -> int:
        return floor(j / 3) + floor(i / 3) * 3

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = [[True for x in range(10)] for _ in range(9)]
        self.cols = [[True for x in range(10)] for _ in range(9)]
        self.boxes = [[True for x in range(10)] for _ in range(9)]
        self.ans_found = False
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != ".":
                    c = ord(self.board[i][j]) - ord('0')
                    self.rows[i][c] = False
                    self.cols[j][c] = False
                    self.boxes[self.get_box_id(i, j)][c] = False
        self.backtrack(0, 0)

Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
