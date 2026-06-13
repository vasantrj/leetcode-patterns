"""
Problem: Weighted Word Mapping
LeetCode ID: 3838
Pattern: Strings / Simulation
Difficulty: Easy

Time Complexity: O(n × m)
Space Complexity: O(n)

Approach:
1. For each word, compute its total weight by summing
   the weight of every character.
2. Take total_weight % 26.
3. Map the result to reverse alphabetical order:
      0  -> 'z'
      1  -> 'y'
      ...
      25 -> 'a'
4. Append the mapped character to the answer.
5. Return the concatenated string.
"""

from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            total = sum(weights[ord(c) - ord('a')] for c in word)
            mod = total % 26
            char = chr(ord('z') - mod)
            result.append(char)
        return ''.join(result)
    