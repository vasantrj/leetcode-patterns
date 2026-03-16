"""
Problem: Group Anagrams
LeetCode ID: 49
Pattern: Hashing / String Sorting
Difficulty: Medium
Time Complexity: O(n * k log k)
Space Complexity: O(n)

Where:
n = number of strings
k = average length of each string

Approach:
1. Use a hashmap where the key represents the sorted characters of a word.
2. For each word:
   - Sort the characters to form a key.
   - Append the word to the list stored at that key.
3. Words that are anagrams will share the same sorted key.
4. Return all grouped values from the hashmap.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())