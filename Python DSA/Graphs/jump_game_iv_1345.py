"""
Problem: Jump Game IV
LeetCode ID: 1345
Pattern: Graphs / BFS
Difficulty: Hard
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Build a hashmap:
   value -> all indices having that value
2. Use BFS to find minimum jumps.
3. From index i, possible moves:
   - i - 1
   - i + 1
   - all indices with same value
4. Use visited set to avoid revisiting indices.
5. Optimization:
   After processing all indices for a value,
   clear that list to prevent repeated work.
6. BFS guarantees minimum jumps.
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        value_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_to_indices[val].append(i)

        visited = set([0])
        queue = deque([0])
        steps = 0

        while queue:
            size = len(queue)
            steps += 1
            for _ in range(size):
                idx = queue.popleft()
                for nxt in (idx - 1, idx + 1):
                    if nxt == n - 1:
                        return steps
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

                val = arr[idx]

                for nxt in value_to_indices[val]:
                    if nxt == n - 1:
                        return steps

                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
                value_to_indices[val].clear()

        return 0
    