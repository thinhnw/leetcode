from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        stack = []
        left = [0 for _ in range(n)]        
        largest = 0
                
        for i, height in enumerate(heights):            
            while len(stack) and height <= stack[-1][0]:
                (min_height, j) = stack.pop()                
                largest = max(largest, min_height * (i - left[j]))
            if len(stack):
                left[i] = stack[-1][1] + 1
            largest = max(largest, height * (i - left[i] + 1))
            stack.append((height, i))

        for (height, i) in stack:
            largest = max(largest, height * (stack[-1][1] - left[i] + 1))

        return largest

print(Solution().largestRectangleArea(heights = [2, 3]))