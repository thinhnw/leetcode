class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zeros] = nums[non_zeros], nums[i]
                non_zeros += 1
        return nums