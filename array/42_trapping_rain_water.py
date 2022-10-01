class Solution:
    def trap(self, height: List[int]) -> int:
        highest = max(height)
        current_height = 0        
        ans = 0                
        
        for i in range(len(height)):
            if height[i] >= highest:
                l = i
                break            
            if height[i] < current_height:
                ans += current_height - height[i]
            else:
                current_height = height[i]
                        
        current_height = 0
        for j in range(len(height)):
            i = len(height) - j - 1
            if height[i] >= highest:
                r = i
                break            
            if height[i] < current_height:
                ans += current_height - height[i]
            else:
                current_height = height[i]
        for i in range(l+1, r):
            ans += highest - height[i]
        return ans
        
            