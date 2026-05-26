"""
Problem: Count the Number of Special Characters I
LeetCode ID: 3120
Pattern: Strings / Hash Set
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Store all lowercase letters in a set.
2. Store all uppercase letters in another set.
3. For each lowercase character:
   - Check whether its uppercase version exists.
4. Count such characters.
5. Return the count.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)
        count = 0
        for ch in lower:
            if ch.upper() in upper:
                count += 1
        return count
    