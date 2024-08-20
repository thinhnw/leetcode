class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        def visit(u):
            visited[u] = True
            if not rooms[u]:
                return
            for v in rooms[u]:
                if not visited[v]:
                    visit(v)
                
        visit(0)
        print(visited)
        return not False in visited

Solution().canVisitAllRooms([[1],[2],[3],[]])