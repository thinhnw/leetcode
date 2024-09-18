class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.string = s
        n = len(s)
        self.is_palindrome = [[-1 for _ in range(n)] for __ in range(n)]
        len_max = 1
        idx = 0
        for l in range(n):
            for r in range(l + len_max, n):
                check = self.checkPalindrome(l, r)
                if check and r - l + 1 > len_max:
                    len_max = r - l + 1
                    idx = l
        return s[idx:idx+len_max]
    
    def checkPalindrome(self, l: int, r: int) -> bool:
        if l >= r:
            return True
        if self.is_palindrome[l][r] >= 0:
            return self.is_palindrome[l][r]
        self.is_palindrome[l][r] = (self.string[l] == self.string[r]) & self.checkPalindrome(l + 1, r - 1)
        return self.is_palindrome[l][r]