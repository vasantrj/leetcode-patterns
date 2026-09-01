"""
Problem: Add Strings
LeetCode ID: 415
Pattern: Strings / Two Pointers / Simulation
Difficulty: Easy

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

Approach:
1. Start from the last character of both strings.
2. Convert each character to its corresponding digit.
3. Add the digits along with the carry.
4. Store the current digit and update the carry.
5. Continue until all digits and the carry are processed.
6. Reverse the collected digits to obtain the final sum.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            total = d1 + d2 + carry
            carry = total // 10
            result.append(str(total % 10))
            i -= 1
            j -= 1
        
        return ''.join(reversed(result))