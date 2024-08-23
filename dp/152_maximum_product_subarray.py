class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_prod = [0 for _ in range(len(nums))]
        max_prod = [0 for _ in range(len(nums))]
        min_prod[0] = max_prod[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                min_prod[i] = max_prod[i] = 0
            elif nums[i] > 0:
                max_prod[i] = max(nums[i], max_prod[i-1] * nums[i])
                min_prod[i] = min(nums[i], min_prod[i-1] * nums[i])
            else:
                max_prod[i] = max(nums[i], min_prod[i-1] * nums[i])
                min_prod[i] = min(nums[i], max_prod[i-1] * nums[i])
        # print(min_prod)
        # print(max_prod) 
        return max(max_prod)
    
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([2,3,-2,4]))