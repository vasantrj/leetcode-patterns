"""
Problem: Check if Strings Can be Made Equal With Operations II
LeetCode ID: 2840
Pattern: Strings / Sorting
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. In one allowed operation, we can swap:
   - any two characters at even indices
   - any two characters at odd indices
2. That means:
   - even-indexed characters can only rearrange among even positions
   - odd-indexed characters can only rearrange among odd positions
3. So for s1 to become equal to s2:
   - sorted(even chars of s1) must equal sorted(even chars of s2)
   - sorted(odd chars of s1) must equal sorted(odd chars of s2)
4. If both match → return True
"""

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_s1 = sorted(s1[::2])
        odd_s1 = sorted(s1[1::2])
        even_s2 = sorted(s2[::2])
        odd_s2 = sorted(s2[1::2])
        return even_s1 == even_s2 and odd_s1 == odd_s2