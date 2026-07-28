"""
Problem: Reverse Vowels of a String
LeetCode ID: 345
Pattern: Strings / Two Pointers
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Convert the string into a list since strings are immutable.
2. Use two pointers:
      - Left starts from the beginning.
      - Right starts from the end.
3. Move each pointer until it points to a vowel.
4. Swap the vowels and continue inward.
5. Convert the list back into a string.
"""

from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        
        while left < right:
            if s_list[left] not in vowels:
                left += 1
            elif s_list[right] not in vowels:
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return "".join(s_list)