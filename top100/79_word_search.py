from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m = len(board)
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]

        self.answer = False

        def backtrack(
            u: int, 
            v: int, 
            board: List[List[str]], 
            visited: List[List[bool]],
            word: str,
        ):
            visited[u][v] = True
            # for row in visited:
            #     print(row)
            # print("\n")
            if not word:
                self.answer = True
                return 
            for d in directions:
                i = u + d[0]
                j = v + d[1]
                if 0 <= i < m and 0 <= j < n and not visited[i][j] and board[i][j] == word[0]:
                    backtrack(i, j, board, visited, word[1:])
                    if self.answer:
                        return

            visited[u][v] = False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    backtrack(i, j, board, visited, word[1:])
        return self.answer
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(Solution().exist(board, word))