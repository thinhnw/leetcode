class Solution(object):
    min_steps = {}
    min_steps[1] = 0
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.min_steps.get(n) is not None:
            return self.min_steps.get(n)
        self.min_steps[n] = n
        for i in range(2, n // 2):
            if n % i == 0:
                self.min_steps[n] = min(self.min_steps[n], self.minSteps(i) + n // i)
        return self.min_steps[n]
                
            


for i in range(1,10):
    print(Solution().minSteps(i))