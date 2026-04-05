"""
Problem: Maximum Walls Destroyed by Robots
LeetCode ID: 3661
Pattern: Dynamic Programming / Binary Search / Memoization
Difficulty: Hard
Time Complexity: O(n log m)
Space Complexity: O(n)

Approach:
1. Sort robots by position along with their shooting distance.
2. Sort the wall positions for binary search.
3. Process robots from right to left using DFS + memoization.
4. For each robot, there are 2 choices:
   - Fire LEFT
   - Fire RIGHT
5. While firing:
   - A bullet can destroy all walls in that direction up to its distance.
   - A bullet stops if it hits another robot.
   - Overlapping wall destruction must be avoided.
6. State:
   - dfs(i, j)
   - i = current robot index
   - j = direction of robot i+1
        0 -> left
        1 -> right
7. Use binary search to count how many walls are destroyed in the valid range.
8. Return the maximum walls destroyed.
"""

from bisect import bisect_left
from functools import cache
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        
        # Sort robots by position, paired with their shooting distance
        arr = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()

        @cache
        def dfs(i: int, j: int) -> int:
            """
            i = current robot index (processing right to left)
            j = firing direction of robot i+1 (0=left, 1=right)
            returns max walls destroyable from robots 0..i
            """
            if i < 0:
                return 0

            pos, dist = arr[i]

            # --- Option 1: Robot i fires LEFT ---
            left = pos - dist
            if i > 0:
                # Physically blocked by robot i-1 on the left
                left = max(left, arr[i - 1][0] + 1)
            l = bisect_left(walls, left)
            r = bisect_left(walls, pos + 1)          # walls <= pos
            walls_left = r - l

            # If robot i fires left, robot i-1 is free to fire in either direction
            # (we pass j=0 meaning: robot i fires left, so robot i-1 sees no constraint from us)
            ans = dfs(i - 1, 0) + walls_left

            # --- Option 2: Robot i fires RIGHT ---
            right = pos + dist
            if i + 1 < n:
                if j == 0:
                    # Next robot fires left → it covers walls down to arr[i+1][0] - arr[i+1][1]
                    # Robot i should not overlap with that range
                    right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1)
                else:
                    # Next robot fires right → robot i is physically blocked at next robot - 1
                    right = min(right, arr[i + 1][0] - 1)

            l = bisect_left(walls, pos)              # walls >= pos
            r = bisect_left(walls, right + 1)
            walls_right = r - l

            ans = max(ans, dfs(i - 1, 1) + walls_right)

            return ans

        result = dfs(n - 1, 1)   # rightmost robot has no robot to its right, j=1 as default
        dfs.cache_clear()
        return result