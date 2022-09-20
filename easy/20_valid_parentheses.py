class Solution:
    def isValid(self, s: str) -> bool:        
        a = []
        for c in s:
            if c in ['(', '{', '[']:
                a.append(c)
            elif c == ')':
                if a.pop() != '(':
                    return False                
            elif c == '}':
                if a.pop() != '{':
                    return False                
            elif c == ']':
                if a.pop() != '[':
                    return False                
        return not bool(a)

print(Solution().isValid("()")) 