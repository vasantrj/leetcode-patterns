"""
Problem: Count the Number of Special Characters II
LeetCode ID: 3121
Pattern: Strings / Hashing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Track:
   - last occurrence of lowercase letters
   - first occurrence of uppercase letters
2. A character is special if:
   - lowercase exists
   - uppercase exists
   - every lowercase appears before uppercase
3. Check all 26 letters.
4. Count valid characters.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                lower = ch.lower()
                if lower not in first_upper:
                    first_upper[lower] = i

        count = 0
        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                count += 1

        return count