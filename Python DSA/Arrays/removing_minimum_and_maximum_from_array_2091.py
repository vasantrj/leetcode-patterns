"""
Problem: Removing Minimum and Maximum From Array
LeetCode ID: 2091
Pattern: Arrays / Greedy
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Find the indices of the minimum and maximum elements.
2. Order their indices so that i < j.
3. There are three possible strategies:
      - Remove both from the front.
      - Remove both from the back.
      - Remove the minimum from the front and maximum from the back.
4. Calculate the deletions required for each strategy.
5. Return the minimum of the three.
"""

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))  
        j = nums.index(max(nums))   
        if i > j:
            i, j = j, i
            
        from_front = j + 1
        from_back = n - i
        both_sides = (i + 1) + (n - j)
        return min(from_front, from_back, both_sides)