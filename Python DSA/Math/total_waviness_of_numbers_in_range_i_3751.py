"""
Problem: Total Waviness of Numbers in Range I
LeetCode ID: 3751
Pattern: Math / Simulation
Difficulty: Easy

Time Complexity: O((num2 - num1 + 1) * D)
Space Complexity: O(D)

Approach:
1. For each number in the range [num1, num2]:
   - Convert it into digits.
2. A digit is considered "wavy" if:
   - It is a peak:
       digit > left neighbor and digit > right neighbor
   - OR it is a valley:
       digit < left neighbor and digit < right neighbor
3. First and last digits cannot be peaks/valleys.
4. Count the waviness of each number and sum the results.
5. Return the total waviness.
"""

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            digits = [int(d) for d in str(n)]
            if len(digits) < 3:
                return 0
            count = 0
            for i in range(1, len(digits) - 1):
                if digits[i] > digits[i-1] and digits[i] > digits[i+1]:
                    count += 1
                elif digits[i] < digits[i-1] and digits[i] < digits[i+1]:
                    count += 1
            return count
        return sum(waviness(n) for n in range(num1, num2 + 1))