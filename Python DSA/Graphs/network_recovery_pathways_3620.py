"""
Problem: Network Recovery Pathways
LeetCode ID: 3620
Pattern: Graphs / Binary Search + DAG DP
Difficulty: Hard

Time Complexity: O((n + m) log m)
Space Complexity: O(n + m)

Approach:
1. Build the DAG and compute its topological order once.
2. Binary search on the minimum allowed edge cost.
3. For a candidate threshold T:
      - Keep only edges with cost >= T.
      - Allow traversal only through online nodes
        (except the source and destination).
4. Using the precomputed topological order, perform
   DP to compute the minimum path cost in the filtered
   graph.
5. If the destination can be reached with total cost
   <= k, the threshold is feasible.
6. Return the largest feasible threshold.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        if not edges:
            return -1

        adj = defaultdict(list)
        indeg = [0] * n
        for u, v, c in edges:
            adj[u].append((v, c))
            indeg[v] += 1

        indeg_copy = indeg[:]
        q = deque([i for i in range(n) if indeg_copy[i] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, c in adj[u]:
                indeg_copy[v] -= 1
                if indeg_copy[v] == 0:
                    q.append(v)

        costs = sorted(set(c for _, _, c in edges))
        target = n - 1

        def feasible(T: int) -> bool:
            dist = [None] * n
            dist[0] = 0
            for u in topo:
                du = dist[u]
                if du is None:
                    continue
                for v, c in adj[u]:
                    if c < T:
                        continue
                    if v != target and not online[v]:
                        continue
                    nd = du + c
                    if nd > k:
                        continue
                    if dist[v] is None or nd < dist[v]:
                        dist[v] = nd
            return dist[target] is not None

        lo, hi = 0, len(costs) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
    