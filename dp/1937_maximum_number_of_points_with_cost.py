class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # for a in points:
        #     print(a)
        # print('---')
        f = points
        m = len(points)
        n = len(points[0])
        for i in range(1, m):
            right = []
            max_right = []
            max_left = 0
            for j in reversed(range(n)):
                right.append(f[i-1][j] - j)
                if len(max_right) == 0:
                    max_right.append(right[-1])
                else:
                    max_right.append(max(max_right[-1], right[-1]))
            # print(list(reversed(right)))
            for j in range(n):
                f[i][j] = max(max_left - j, max_right[-1] + j) + points[i][j]
                max_left = max(max_left, right.pop() + j + j)
                max_right.pop()
        # for a in f:
        #     print(a)
        print(max(f[m-1]))
        return max(f[m-1])
    

Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]])
Solution().maxPoints([[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]) #15
Solution().maxPoints([[5,2,1,2],[2,1,5,2],[5,5,5,0]]) #13
Solution().maxPoints([[4,3,2,1],[1,4,3,0],[0,0,1,5],[1,5,3,4],[0,3,3,4]]) #18
