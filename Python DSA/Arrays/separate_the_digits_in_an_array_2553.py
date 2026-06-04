"""
Problem: Separate the Digits in an Array
LeetCode ID: 2553
Pattern: Arrays / Simulation
Difficulty: Easy
Time Complexity: O(total digits)
Space Complexity: O(total digits)

Approach:
1. Traverse each number in nums.
2. Convert the number into digits.
3. Append each digit individually to the answer list.
4. Maintain original digit order.
5. Return the final digit array.
"""

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for digit in str(num):
                result.append(int(digit))
        return result  
        