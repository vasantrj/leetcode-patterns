"""
Problem: Self Dividing Numbers
LeetCode ID: 728
Pattern: Mathematics / Digit Manipulation
Difficulty: Easy

Time Complexity: O((right - left + 1) × d)
Space Complexity: O(1) auxiliary space

where:
    d = number of digits in each number

Approach:
1. Check every number in the given range.
2. Extract each digit using modulo 10.
3. A number is self-dividing if:
      - It contains no zero digit.
      - The number is divisible by every one of its digits.
4. Add every valid number to the result.
"""

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            n = num
            while n > 0:
                digit = n % 10
                if digit == 0 or num % digit != 0:
                    return False
                n //= 10
            return True
        
        return [num for num in range(left, right + 1) if is_self_dividing(num)]