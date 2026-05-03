"""
Problem: Sum of Primes Between Number and Its Reverse
Pattern: Math / Prime Checking
Difficulty: Easy-Medium
Time Complexity: O(n * sqrt(n))
Space Complexity: O(1)

Approach:
1. Reverse the number.
2. Find the range [lo, hi] between n and reversed(n).
3. For each number in the range:
   - Check if it is prime using sqrt(n) optimization.
4. Sum all prime numbers in that range.
5. Return the total sum.
"""

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        lo, hi = min(n, r), max(n, r)
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True
        return sum(x for x in range(lo, hi + 1) if is_prime(x))