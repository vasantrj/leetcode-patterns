"""
Problem: Add Binary
LeetCode ID: 67
Pattern: Strings / Simulation
Difficulty: Easy
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

Approach:
1. Traverse both binary strings from right to left.
2. Maintain carry during addition.
3. At each step:
   - Add current bits + carry
   - Append sum % 2 to answer
   - Update carry = sum // 2
4. Reverse final result and return.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))