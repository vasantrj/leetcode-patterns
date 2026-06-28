"""
Problem: Maximum Element After Decreasing and Rearranging
LeetCode ID: 1846
Pattern: Greedy / Sorting
Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort the array since rearranging is allowed.
2. Set the first element to 1.
3. Traverse the remaining elements:
      - If the current value is larger than the previous value + 1,
        decrease it to previous + 1.
      - Otherwise, keep it unchanged.
4. The last element will be the maximum possible value after all
   adjustments.

Why Greedy Works:
Sorting places smaller values first, allowing larger values to be
used later. At each position, assigning:

    min(current_value, previous + 1)

produces the largest valid value while satisfying the constraints.
Since every position is maximized greedily, the last element is also
maximized.
"""

from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1] + 1)
        return arr[-1]
        