"""
Problem: Sum Game
LeetCode ID: 1927
Pattern: Game Theory / Mathematics
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Split the string into two equal halves.
2. Calculate the digit sum and number of '?' characters
   in each half.
3. If the total number of '?' characters is odd, Alice
   can always force a win.
4. Otherwise, Bob can win only when the existing sum
   difference can be exactly balanced by the '?' digits.
5. In every other case, Alice wins.
"""

class Solution:
    def sumGame(self,num: str) -> bool:
        n = len(num)
        half = n // 2
        left_sum = 0
        left_count = 0
        right_sum = 0
        right_count = 0

        for i in range(half):
            if num[i] == "?":
                left_count += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == "?":
                right_count += 1
            else:
                right_sum += int(num[i])

        if (left_count + right_count) % 2 == 1:
            return True

        if (2 * (left_sum - right_sum)== 9 * (right_count - left_count)):
            return False
        return True