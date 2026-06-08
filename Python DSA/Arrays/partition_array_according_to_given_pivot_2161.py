"""
Problem: Partition Array According to Given Pivot
LeetCode ID: 2161
Pattern: Arrays / Partitioning
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Traverse the array once.
2. Store:
   - elements smaller than pivot
   - elements equal to pivot
   - elements greater than pivot
3. Concatenate the three lists.
4. Relative order within each group is preserved.
"""

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return less + equal + greater