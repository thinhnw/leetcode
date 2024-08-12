class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 1
        while i >= 0:
            j = i
            while j >= 0 and nums[j] != 0:
                j -= 1
            if j < 0:
                break
            for k in range(j, i):
                nums[k], nums[k+1] = nums[k+1], nums[k]
            i -= 1
        return nums 