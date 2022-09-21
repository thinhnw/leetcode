class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0  
        a = [ True for _ in range(len(s)) ]
        for i in range(len(s)):
            c = s[i]            
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0:
                    a[i] = False
                else:
                    count -= 1
        count = 0
        for i in reversed(range(len(s))):
            if not a[i]:
                continue
            c = s[i]
            if c == ')':
                count += 1
            elif c == '(':
                if count == 0:
                    a[i] = False
                else:
                    count -= 1
        t = ""            
        for i in range(len(s)):
            if a[i]:
                t += s[i]
                
        return t
        