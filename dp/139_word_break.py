class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)
        str_match = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i + len(wordDict[j]) <= n and s[i:i+len(wordDict[j])] == wordDict[j]:
                    str_match[i][i + len(wordDict[j]) - 1] = True
        
        can_break = [[-1 for _ in range(n)] for _ in range(n)]
        def check(l: int, r: int) -> bool:
            if l == r:
                return str_match[l][r]
            if can_break[l][r] != -1:
                return can_break[l][r]
            if str_match[l][r]:
                can_break[l][r] = True
                return True
            can_break[l][r] = False
            for mid in range(l, r):
                if check(l, mid) and check(mid + 1, r):
                    can_break[l][r] = True
                    return True
            #print(l, r, can_break[l][r])
            return False
        
        return check(0, n-1)