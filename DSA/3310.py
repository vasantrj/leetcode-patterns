"""
Problem: Remove Methods From Project
LeetCode ID: 3310
Pattern: Graph / BFS
Difficulty: Medium

Time Complexity: O(n + m)
Space Complexity: O(n + m)

where:
    n = number of methods
    m = number of invocations

Approach:
1. Build the directed graph representing method invocations.
2. Perform BFS starting from the suspicious method k to
   mark every reachable (suspicious) method.
3. Check every invocation:
      - If a safe method calls a suspicious method,
        the suspicious methods cannot be removed.
        Return all methods.
4. Otherwise, return every method that is not marked
   suspicious.
"""

from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for caller, called in invocations:
            graph[caller].append(called)

        suspicious = [False] * n
        suspicious[k] = True
        queue = [k]
        index = 0
        while index < len(queue):
            method = queue[index]
            index += 1
            for called in graph[method]:
                if not suspicious[called]:
                    suspicious[called] = True
                    queue.append(called)

        for caller, called in invocations:
            if not suspicious[caller] and suspicious[called]:
                return list(range(n))

        return [method for method in range(n) if not suspicious[method]]
