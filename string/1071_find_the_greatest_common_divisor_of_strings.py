class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def is_divided(s, t):
            if len(s) < len(t) or len(s) % len(t) != 0:
                return False
            t = t * (len(s) // len(t))
            return s == t

        max_len = min(len(str1), len(str2))
        for i in range(max_len, 0, -1):
            t = str1[:i]
            if is_divided(str1, t) and is_divided(str2, t):
                return t

        return ""
