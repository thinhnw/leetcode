class Solution:
    def check_palindrome(self, l, r) -> bool:
        if l >= r:
            return True
        if self.is_palindrome[l][r] != -1:
            return self.is_palindrome[l][r]
        self.is_palindrome[l][r] = (self.s[l] == self.s[r]) & self.check_palindrome(l + 1, r - 1)
        return self.is_palindrome[l][r]
    
    def findMinCut(self, l) -> int:
        if self.check_palindrome(l, len(self.s) - 1):
            return 0
        if self.f[l] != -1:
            return self.f[l]
        res = 4_000_000
        for r in range(l, len(self.s) - 1):
            if self.check_palindrome(l, r):
                res = min(res, self.findMinCut(r + 1) + 1)
        self.f[l] = res
        return res

    def minCut(self, s: str) -> int:
        self.s = s
        self.is_palindrome = [[-1 for j in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                self.is_palindrome[i][j] = self.check_palindrome(i, j)
        self.f = [-1 for j in range(len(s))]
        return self.findMinCut(0)

print(Solution().minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))