class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_sum = 0
        curr_sum = 0
        longest = 0
        for num in nums:
            if not num:
                prev_sum = curr_sum
                curr_sum = 0
            else:
                curr_sum += 1
                longest = max(longest, prev_sum + curr_sum)
        return longest - (1 if longest == len(nums) else 0)