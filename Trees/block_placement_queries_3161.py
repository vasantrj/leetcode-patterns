"""
Problem: Block Placement Queries
LeetCode ID: 3161
Pattern: Segment Tree / Sorted List
Difficulty: Hard

Time Complexity: O(q log n)
Space Complexity: O(n)

Approach:
1. Maintain obstacle positions using SortedList:
   - Quickly find previous and next obstacles.
2. Use Segment Tree:
   - Stores maximum available gap ending at each obstacle.
3. Query Type 1:
   - Insert a new obstacle.
   - Split an existing gap into two smaller gaps.
   - Update segment tree.
4. Query Type 2:
   - Check if block of size sz can fit in [0, x].
   - Check:
       a) Current free gap before x.
       b) Maximum stored gap before previous obstacle.
5. Return results for all type 2 queries.
"""

from typing import List
from sortedcontainers import SortedList


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = max(q[1] for q in queries) + 1

        # Segment tree storing maximum gap
        tree = [0] * (4 * max_x)

        def update(node, start, end, idx, left_obstacle):
            if start == end:
                tree[node] = idx - left_obstacle
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, left_obstacle)
            else:
                update(node * 2 + 1, mid + 1, end, idx, left_obstacle)

            tree[node] = max(tree[node * 2], tree[node * 2 + 1])

        def query(node, start, end, left, right):
            if right < start or end < left:
                return 0

            if left <= start and end <= right:
                return tree[node]

            mid = (start + end) // 2

            return max(
                query(node * 2, start, mid, left, right),
                query(node * 2 + 1, mid + 1, end, left, right)
            )

        obstacles = SortedList([0, max_x])

        # Initial empty range
        update(1, 0, max_x, max_x, 0)

        result = []

        for q in queries:

            # Add obstacle
            if q[0] == 1:
                x = q[1]

                idx = obstacles.bisect_left(x)

                left = obstacles[idx - 1]
                right = obstacles[idx]

                obstacles.add(x)

                # Update split gaps
                update(1, 0, max_x, x, left)
                update(1, 0, max_x, right, x)

            # Check placement
            else:
                x = q[1]
                size = q[2]

                idx = obstacles.bisect_right(x)

                left = obstacles[idx - 1]

                # Space between last obstacle and x
                gap = x - left

                if gap >= size:
                    result.append(True)

                else:
                    max_gap = query(
                        1,
                        0,
                        max_x,
                        1,
                        left
                    )

                    result.append(max_gap >= size)

        return result