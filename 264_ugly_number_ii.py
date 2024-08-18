class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * n
        f[0] = 1
        for i in range(1, n):
            nums = []
            f[i] = f[i-1] * 2
            for j in range(i):
                if f[j] * 2 >= f[i]:
                    break
                if f[j] * 2 > f[i-1]:
                    f[i] = min(f[i], f[j] * 2)
                    break
                elif f[j] * 3 > f[i-1]:
                    f[i] = min(f[i], f[j] * 3)
                elif f[j] * 5 > f[i-1]:
                    f[i] = min(f[i], f[j] * 5)
        return f[-1]