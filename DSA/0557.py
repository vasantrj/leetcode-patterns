"""
Problem: Reverse Words in a String III
LeetCode ID: 557
Pattern: Strings / String Manipulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Split the string into words using a space as the delimiter.
2. Reverse each word individually using Python string slicing:
   - word[::-1] reverses the characters of the word.
3. Join all reversed words back together using a single space.
4. Using split(' ') preserves the original spacing between words as
   required by the problem.
5. Return the resulting string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))


    