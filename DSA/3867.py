"""
Problem: Sum of GCD of Formed Pairs
LeetCode ID: 3867
Pattern: Mathematics / GCD / Sorting
Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Traverse the array while maintaining the maximum
   value seen so far.
2. For each element, compute the GCD of the element
   and the current maximum, storing the results.
3. Sort the resulting GCD values.
4. Pair the smallest value with the largest, the
   second smallest with the second largest, and so on.
5. Sum the GCD of every formed pair and return the
   final answer.
"""

from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        for i, x in enumerate(nums):
            mx = max(mx, x)
            prefix_gcd[i] = gcd(x, mx)

        prefix_gcd.sort()
        ans = 0
        l, r = 0, n - 1
        while l < r:
            ans += gcd(prefix_gcd[l], prefix_gcd[r])
            l += 1
            r -= 1
        return ans

        