import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]", "", s).lower()
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))