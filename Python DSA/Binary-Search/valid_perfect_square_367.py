"""
Problem: Valid Perfect Square
LeetCode ID: 367
Pattern: Binary Search
Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Search for the square root of num using binary search.
2. Calculate the square of the middle value.
3. If mid * mid equals num, num is a perfect square.
4. If mid * mid is smaller than num, search the right half.
5. Otherwise, search the left half.
6. If no value produces num, return False.
"""

class Solution:
    def isPerfectSquare(self,num: int) -> bool:
        if num < 1:
            return False
        left = 1
        right = num
        while left <= right:
            middle = (
                left + right
            ) // 2
            square = middle * middle
            if square == num:
                return True
            elif square < num:
                left = middle + 1
            else:
                right = middle - 1
        return False