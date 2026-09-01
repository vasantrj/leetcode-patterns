"""
Problem: Maximum Total Subarray Value II
LeetCode ID: 3691
Pattern: Greedy / Heap / Sparse Table (RMQ)
Difficulty: Hard

Time Complexity: O(n log n + k log k)
Space Complexity: O(n log n + k)

Approach:
1. Build Sparse Tables for range minimum and maximum queries.
2. Query any subarray value:
      max(subarray) - min(subarray)
   in O(1) time.

3. Use a max-heap to lazily generate the k largest
   subarray values.

4. Start with the full interval [0, n-1].

5. Each time we pop the current best interval [l, r]:
   - Add its value to the answer.
   - Generate two children:
       [l+1, r]
       [l, r-1]

6. Use a visited set to avoid processing the same
   interval multiple times.

7. Repeat k times and return the total.
"""

from typing import List
import math
import heapq


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = max(1, math.floor(math.log2(n)) + 1)
        mn = [[0] * n for _ in range(LOG)]
        mx = [[0] * n for _ in range(LOG)]
        mn[0] = nums[:]
        mx[0] = nums[:]
        for j in range(1, LOG):
            length = 1 << j
            for i in range(n - length + 1):
                mn[j][i] = min(
                    mn[j - 1][i],
                    mn[j - 1][i + (1 << (j - 1))]
                )
                mx[j][i] = max(
                    mx[j - 1][i],
                    mx[j - 1][i + (1 << (j - 1))]
                )
        def query(l: int, r: int) -> int:
            length = r - l + 1
            p = math.floor(math.log2(length))
            maximum = max(
                mx[p][l],
                mx[p][r - (1 << p) + 1]
            )
            minimum = min(
                mn[p][l],
                mn[p][r - (1 << p) + 1]
            )
            return maximum - minimum
        visited = set()
        heap = []
        def push(l: int, r: int) -> None:
            if l < 0 or r >= n or l > r:
                return
            if (l, r) in visited:
                return
            visited.add((l, r))
            heapq.heappush(
                heap,
                (-query(l, r), l, r)
            )
        push(0, n - 1)
        total = 0
        count = 0
        while heap and count < k:
            value, l, r = heapq.heappop(heap)
            total -= value
            count += 1
            push(l + 1, r)
            push(l, r - 1)
        return total
    