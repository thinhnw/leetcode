class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * n
        f[0] = 1
        for i in range(1, n):
            for j in range(i):
                if f[j] * 2 > f[i-1]:
                    a = f[j] * 2
                    break
            for j in range(i):
                if f[j] * 3 > f[i-1]:
                    b = f[j] * 3
                    break
            for j in range(i):
                if f[j] * 5 > f[i-1]:
                    c = f[j] * 5
                    break
            f[i] = min(a, b, c)

        return f[-1]
print(Solution().nthUglyNumber(10))