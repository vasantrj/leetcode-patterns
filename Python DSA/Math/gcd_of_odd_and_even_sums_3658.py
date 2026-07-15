"""
Problem: GCD of Odd and Even Sums
LeetCode ID: 3658
Pattern: Mathematics / Number Theory
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. The sum of the first n odd numbers is:
       n²
2. The sum of the first n even numbers is:
       n(n + 1)
3. Therefore:
       gcd(n², n(n + 1))
     = n × gcd(n, n + 1)
4. Since consecutive integers are always coprime,
   gcd(n, n + 1) = 1.
5. Hence, the answer is simply n.
"""


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
    
    