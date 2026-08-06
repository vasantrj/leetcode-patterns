"""
Problem: Smallest Divisible Digit Product I
LeetCode ID: 3345
Pattern: Brute Force / Mathematics
Difficulty: Easy

Time Complexity: O(k × d)

where:
    k = numbers checked
    d = number of digits

Space Complexity: O(1)

Approach:
1. Start checking numbers from n.
2. Compute the product of the digits of the current number.
3. If the product is divisible by t, return the number.
4. Otherwise, increment the number and repeat.
"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(x: int) -> int:
            p = 1
            while x > 0:
                p *= x % 10
                x //= 10
            return p
        num = n
        while digitProduct(num) % t != 0:
            num += 1
        return num
    