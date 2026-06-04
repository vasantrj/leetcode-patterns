"""
Problem: Fizz Buzz
LeetCode ID: 412
Pattern: Math / Simulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Iterate from 1 to n.
2. For each number:
   - If divisible by both 3 and 5 -> "FizzBuzz"
   - Else if divisible by 3 -> "Fizz"
   - Else if divisible by 5 -> "Buzz"
   - Else convert number to string
3. Append result to answer list.
4. Return final list.
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans