class Solution:
    # def calc(self, i, k):
        
    #     if s[i] == '(':
    #         if self.calc(i - 1, k - 1) != -1:
    #             self.f[i][k] =  self.calc(i - 1, k - 1) + 1
    #         else:
    #             self.f[i][k] = -1
    #     else:
    #         if self.calc()
    def longestValidParentheses(self, s: str) -> int:
        # f[i][k]: longest length if there is a substring that ends at i and have k open brackets else 0
        # f[i][k] >= k
        # res: max(f[0])
        # f[i][k] = f[i - 1][k - 1] + 1 if s[i] == '(' else f[i - 1][k + 1] + 1
        if not s:
            return 0
        n = len(s)
        res = 0
        f = [-1 for _ in range((n >> 1) + 1)]
        f[0] = 0
        for i in range(n):
            if s[i] == '(':
                for k in reversed(range(1,(n >> 1) + 1)):
                    if f[k - 1] != -1:
                        f[k] = f[k - 1] + 1
                    else:
                        f[k] = -1
                f[0] = 0
            else:
                for k in range(1, (n>>1) + 1):
                    if f[k] != -1:
                        f[k - 1] = f[k] + 1
                    elif k - 1:
                        f[k - 1] = -1
                    else:
                        f[0] = 0
            # print(f)
            res = max(res, f[0])
        return res

Solution().longestValidParentheses(")()())()()(")
        
