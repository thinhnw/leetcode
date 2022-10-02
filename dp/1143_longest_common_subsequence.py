class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # f[i][j]: longest common subsequence of text1[:i] and text2[:j]
        # res: f[m-1][n-1]
        # f[i][j] = max(f[i - 1][j], f[i][j - 1]) + bool(text1[i] == text2[j])
        m = len(text1)
        n = len(text2)
        f = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                f[i][j] = max(max(f[i][j-1], f[i-1][j]), f[i-1][j-1] + bool(text1[i] == text2[j]))
        return f[m - 1][n - 1]

print(Solution().longestCommonSubsequence("abcde",  "ace"))