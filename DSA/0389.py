"""
Problem: Find the Difference
LeetCode ID: 389
Pattern: Bit Manipulation / XOR
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. XOR the ASCII value of every character in s and t.
2. Matching characters cancel because:
      x ^ x = 0
3. The extra character remains after all pairs cancel.
4. Convert the resulting ASCII value back to a character.
"""

class Solution:
    def findTheDifference(self,s: str,t: str) -> str:
        result = 0
        for character in s:
            result ^= ord(character)
        for character in t:
            result ^= ord(character)
        return chr(result)
    