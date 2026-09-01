"""
Problem: Count Subarrays With Majority Element II
LeetCode ID: 3739
Pattern: Prefix Sum / Ordered Set
Difficulty: Hard

Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Transform the array:
      target     -> +1
      non-target -> -1
2. Compute the running prefix sum.
3. A subarray has target as the majority iff:
      prefix[r + 1] - prefix[l] > 0
   which is equivalent to:
      prefix[l] < prefix[r + 1]
4. Maintain all previous prefix sums in a sorted list.
5. For each prefix sum, use binary search to count
   how many previous prefix sums are smaller.
6. Insert the current prefix sum into the sorted list.
"""

from typing import List
from sortedcontainers import SortedList


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        prefix = 0
        sorted_prefixes = SortedList([0])
        for num in nums:
            prefix += 1 if num == target else -1
            result += sorted_prefixes.bisect_left(prefix)
            sorted_prefixes.add(prefix)
        return result

        