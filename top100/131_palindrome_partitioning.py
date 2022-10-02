from typing import List
class Solution:
    def check_palindrome(self, s) -> bool:
        if not s:
            return False
        for i in range(len(s) >> 1):
            if s[i] != s[-i - 1]:
                return False
        return True
    def backtrack(self, i):
        if i == len(self.s):
            self.res.append([])
            for r in self.cur:
                self.res[-1].append(self.s[r[0]:r[1] + 1])
            return
        for j in range(i, len(self.s)):
            if self.is_palindrome[i][j]:
                self.cur.append([i, j])
                self.backtrack(j + 1)
                self.cur.pop()
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.is_palindrome = [[False for j in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                self.is_palindrome[i][j] = self.check_palindrome(s[i:j+1])
            # print(self.is_palindrome[i]) 
        self.res = []
        self.cur = []
        self.backtrack(0)
        return self.res

print(Solution().partition("aab"))