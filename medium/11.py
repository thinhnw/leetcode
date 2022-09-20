height = [1,8,6,2,5,4,8,3,7]
# height = [1, 1]
# height = [4,3,2,1,4]
# height = [2,3,4,5,18,17,6]
class Solution:
    def __init__(self):
      pass
    def f(self, height):
        stack = [0]
        ans = 0
        for i in range(1, len(height)):
            l = 0
            r = len(stack) - 1
            while l < r:
                mid = l + ((r - l) >> 1)
                if height[i] > height[stack[mid]]:
                    l =  mid + 1
                else:
                    r = mid
                print(i, l, r, mid)
            if height[i] <= height[stack[r]]:
              ans = max(ans, (i - stack[r]) * height[i])
            if height[i] > height[stack[-1]]:
                stack.append(i)
        return ans

    def maxArea(self, height):
     
        return max(self.f(height), self.f(height[::-1]))

a = Solution()
print(a.maxArea(height))