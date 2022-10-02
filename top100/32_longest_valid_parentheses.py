class Solution:
    def calc(self, i, k):
        if i == -1:
            return 0 if not k else -1
        if k in self.f[i]:
            return self.f[i][k]
        if self.s[i] == '(':
            if k == 0:
                self.f[i][k] = 0
            elif self.calc(i - 1, k - 1) != -1:
                self.f[i][k] =  self.calc(i - 1, k - 1) + 1
            else:
                self.f[i][k] = -1
        else:
            if self.calc(i - 1, k + 1) != -1:
                self.f[i][k] = self.calc(i - 1, k + 1) + 1
            elif k:
                self.f[i][k] = -1
            elif not k:
                self.f[i][k] = 0
        return self.f[i][k]
    def longestValidParentheses(self, s: str) -> int:
        # f[i][k]: longest length if there is a substring that ends at i and have k open brackets else 0
        # f[i][k] >= k
        # res: max(f[0])
        # f[i][k] = f[i - 1][k - 1] + 1 if s[i] == '(' else f[i - 1][k + 1] + 1
        if not s:
            return 0
        n = len(s)
        res = 0
        self.s = s
        self.f = [{} for _ in range(n)]
        for i in range(n):
            res = max(res, self.calc(i, 0))
        # for i in range(n):
        #     print(self.f[i])
        # print(self.calc(0, 1))
        return res

print(Solution().longestValidParentheses(")()())()()("))
        
