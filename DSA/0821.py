"""
Problem: Shortest Distance to a Character
LeetCode ID: 821
Pattern: Arrays / Two Passes / Greedy
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Create a result array to store the shortest distance from each
   position to the nearest occurrence of character c.
2. Traverse the string from left to right:
   - Keep track of the most recent position of c using prev.
   - The distance to the nearest c on the left is i - prev.
3. Traverse the string from right to left:
   - Keep track of the most recent position of c from the right.
   - The distance to the nearest c on the right is prev - i.
   - Take the minimum of the left and right distances.
4. After both passes, result[i] contains the shortest distance from
   index i to any occurrence of c.
"""

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        previous = float("-inf")
        for i in range(n):
            if s[i] == c:
                previous = i
            result[i] = i - previous
        previous = float("inf")
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                previous = i
            result[i] = min(result[i], previous - i)
        return result