from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = set()

        adj = [[] for _ in range(n)]
        for u, v, w in times:
            adj[u - 1].append((v - 1, w))

        d = [1_000_000_000 for _ in range(n)]
        d[k - 1] = 0
        pq.add((0, k - 1))
        while len(pq):
            distance, u = min(pq)
            pq.remove((distance, u))
            for v, w in adj[u]:
                if d[v] > distance + w:
                    d[v] = distance + w 
                    pq.add((d[v], v))
        res = 0 
        for i in range(n):
            print(i, d[i])
            res = max(res, d[i])
        return res if res != 1_000_000_000 else -1

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 3))