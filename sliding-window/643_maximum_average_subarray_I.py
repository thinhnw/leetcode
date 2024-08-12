class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        sum_k = 0
        for i in range(k):
            sum_k += nums[i]
        ans = float(sum_k) / k

        i = 0
        j = k
        while i < j < len(nums):
            sum_k = float(sum_k + nums[j] - nums[i])
            ans = max(ans, sum_k / k)
            i += 1
            j += 1
        return ans

# print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
# print(Solution().findMaxAverage([4,2,1,3,3], 2))
# print(Solution().findMaxAverage([7,4,5,8,8,3,9,8,7,6], 7))