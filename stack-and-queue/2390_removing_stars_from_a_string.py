class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = []
        for c in s:
            if c != '*':
                t.append(c)
            elif len(t):
                t.pop()
        return ''.join(t)