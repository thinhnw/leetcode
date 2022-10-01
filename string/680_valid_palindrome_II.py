import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(s, len(s))
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                if self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1]):
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return True

print(Solution().validPalindrome("abc"))