class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        f = [[-1 for _ in range(m)] for _ in range(n+1)]

        def check(i: int, j: int) -> bool:
            if j == -1:
                return i == -1
            if f[i][j] != -1:
                return f[i][j]
            if i == -1:
                f[i][j] = check(i, j-2) if p[j] == '*' else False
                return f[i][j]

            if p[j].isalpha():
                f[i][j] = check(i-1, j-1) if s[i] == p[j] else False
            elif p[j] == '.':
                f[i][j] = check(i-1, j-1)
            elif p[j] == '*':
                if s[i] == p[j-1]:
                    f[i][j] = check(i-1, j) or check(i-1, j-2)
                elif p[j-1] == '.':
                    f[i][j] = check(i-1, j) or check(i-1, j-2) or check(i, j-2)    
                else:
                    f[i][j] = check(i, j-2)

            return f[i][j]

        for i in range(n):
            for j in range(m):
                print(i, j, check(i, j))
                check(i, j)
        return f[n-1][m-1]

print(Solution().isMatch("baabbbaccbccacacc", "c*..b*a*a.*a..*c")) 