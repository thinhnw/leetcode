class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        last = {}
        f0 = 1
        ans = 1
        last[s[0]] = 0
        for i in range(1, len(s)):          
            if s[i] in last:
                f = min(i - last[s[i]], f0 + 1)
            else:
                f = f0 + 1
            # print(i, f, last.get(s[i]))
            ans = max(ans, f)
            f0 = f
            last[s[i]] = i

        return ans
print(Solution().lengthOfLongestSubstring("abcabcbb"))