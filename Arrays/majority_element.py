"""
Problem: Majority Element
LeetCode ID: 169
Pattern: Boyer-Moore Voting Algorithm
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use Boyer-Moore Voting Algorithm.
2. Maintain a candidate and a count.
3. If count becomes 0, choose the current number as the new candidate.
4. If the current number equals the candidate, increment count.
5. Otherwise decrement count.
6. Since the majority element appears more than n/2 times, the final candidate will be the answer.
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate