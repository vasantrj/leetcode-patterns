"""
Problem: Sqrt(x)
LeetCode ID: 69
Pattern: Binary Search
Difficulty: Easy

Time Complexity: O(log x)
Space Complexity: O(1)

Approach:
1. Handle the edge cases where x is 0 or 1.
2. Perform binary search on the range [1, x // 2].
3. For each middle value:
      - If mid² == x, return mid.
      - If mid² < x, search the right half.
      - Otherwise, search the left half.
4. If no perfect square is found, return the largest
   integer whose square is less than x.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
    
    