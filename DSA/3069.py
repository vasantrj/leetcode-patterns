"""
Problem: Distribute Elements Into Two Arrays I
LeetCode ID: 3069
Pattern: Arrays / Simulation
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Put the first element into arr1 and the second element
   into arr2.
2. For every remaining element:
      - If the last element of arr1 is greater than the
        last element of arr2, append it to arr1.
      - Otherwise, append it to arr2.
3. Concatenate arr1 and arr2 to form the final result.
"""

from typing import List

class Solution:
    def resultArray(self,nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for number in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(number)
            else:
                arr2.append(number)
        return arr1 + arr2