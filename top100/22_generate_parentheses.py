from typing import List
class Solution:    
    def generateParenthesis(self, n: int) -> List[str]:        
        res = []        
        for x in range(1 << (n << 1)):
            stack = 0
            check = True
            st = []
            for k in range(n << 1):
                # print(x, k, "kth =>", (1 << k) & x)
                if (1 << k) & x:
                    stack += 1
                    st.append("(")
                else:
                    if not stack:
                        check = False
                        break
                    stack -= 1
                    st.append(")")
            # print(x, "".join(st))
            if check and not stack:
                res.append("".join(st))

        return res
print(Solution().generateParenthesis(3))