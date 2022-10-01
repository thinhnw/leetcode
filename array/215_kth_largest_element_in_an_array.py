class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lowest = -10000
        highest = 10000
        c = {}
        for i in range(lowest, highest + 1):
            c[i] = 0
        for i in nums:
            c[i] += 1
        
        for i in reversed(range(lowest, highest + 1)):
            if c[i]:
                k -= c[i]
                if k <= 0:
                    return i
                