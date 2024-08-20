class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        m = len(maze)
        n = len(maze[0]) 
        INF = 100000
        distance = [[INF for _ in range(n)] for __ in range(m)]
        distance[entrance[0]][entrance[1]] = 0
        # for i in distance:
        #     print(i)
        q = [entrance]
        ans = INF
        while len(q):
            (u, v) = q.pop(0)
            if u == 0 or u == m-1 or v == 0 or v == n-1:
                if [u, v] != entrance:
                    ans = min(ans, distance[u][v])
            for k in range(4):
                next_u = u + di[k]
                next_v = v + dj[k]
                # print("next", next_u, next_v)
                if 0 <= next_u < m and 0 <= next_v < n:
                    # print("dist", distance[next_u][next_v])
                    if maze[next_u][next_v] == '.' and distance[next_u][next_v] > distance[u][v] + 1:
                        distance[next_u][next_v] = distance[u][v] + 1
                        q.append((next_u, next_v))
        # for i in distance:
        #     print(i)
        if ans == INF:
            return -1
        return ans
    
# print(Solution().nearestExit( maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
# print(Solution().nearestExit( maze = [['.'],['.']], entrance = [1,0]))
print(Solution().nearestExit(maze=[["+",".","+"],[".",".","."],["+",".","+"]], entrance=[1,2]))