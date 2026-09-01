"""
Problem: Rotated Digits
LeetCode ID: 788
Pattern: Math / Digit Check
Difficulty: Medium
Time Complexity: O(n * d)
Space Complexity: O(1)

Approach:
1. A number is valid if:
   - After rotation, it becomes a different valid number.
2. Valid rotations:
   0→0, 1→1, 2→5, 5→2, 6→9, 8→8, 9→6
3. Invalid digits:
   3, 4, 7 → number becomes invalid
4. Good number conditions:
   - Contains at least one of {2,5,6,9}
   - Contains no invalid digits
5. Iterate from 1 to n and count valid numbers.
"""

class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_diff = {2, 5, 6, 9}
        invalid = {3, 4, 7}
        count = 0
        for num in range(1, n + 1):
            x = num
            has_diff = False
            is_valid = True
            while x > 0:
                digit = x % 10
                if digit in invalid:
                    is_valid = False
                    break
                if digit in valid_diff:
                    has_diff = True
                x //= 10
            if is_valid and has_diff:
                count += 1
        return count
    