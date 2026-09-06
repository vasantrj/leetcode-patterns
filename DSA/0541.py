"""
Problem: Reverse String II
LeetCode ID: 541
Pattern: Strings / Array Manipulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Convert the string into a list because strings are immutable in Python.
2. Traverse the string in blocks of size 2k.
3. For each block:
   - Reverse the first k characters.
   - Leave the next k characters unchanged.
   - If fewer than k characters remain, reverse all remaining characters.
4. Use slice assignment to replace the first k characters with their
   reversed order.
5. Convert the modified character list back into a string and return it.
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        characters = list(s)
        n = len(characters)
        for i in range(0, n, 2 * k):
            characters[i:i + k] = reversed(characters[i:i + k])
        return "".join(characters)

    