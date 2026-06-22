"""
Problem: Maximum Number of Balloons
LeetCode ID: 1189
Pattern: Hash Map / Counting
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Count the frequency of every character in the string.
2. The word "balloon" requires:
      b -> 1
      a -> 1
      l -> 2
      o -> 2
      n -> 1
3. Compute how many times each required character
   can contribute.
4. The answer is the minimum among these counts.
"""

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count['b'],count['a'],count['l'] // 2,count['o'] // 2,count['n'])
    
