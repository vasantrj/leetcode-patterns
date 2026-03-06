"""
Problem: Contains Duplicate
LeetCode ID: 217
Pattern: Hashing / Set
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a set to track numbers we have already seen.
While iterating through the array:
- If the number is already in the set, a duplicate exists → return True.
- Otherwise add the number to the set.

If we finish the loop without finding duplicates, return False.
"""

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    