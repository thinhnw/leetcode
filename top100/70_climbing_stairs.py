class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = 1
        f1 = 1
        fi = 1
        for i in range(2, n + 1):
            fi = f0 + f1
            f0 = f1
            f1 = fi
        return fi