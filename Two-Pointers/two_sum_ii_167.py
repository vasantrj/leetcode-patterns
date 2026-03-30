"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode ID: 167
Pattern: Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Since the array is already sorted, use two pointers:
   - left at the start
   - right at the end
2. Compute the sum of numbers[left] + numbers[right].
3. If the sum == target → return 1-based indices.
4. If the sum < target → move left pointer rightward.
5. If the sum > target → move right pointer leftward.
6. Continue until the correct pair is found.
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []