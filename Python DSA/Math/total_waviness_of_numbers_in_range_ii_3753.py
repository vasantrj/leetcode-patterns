"""
Problem: Total Waviness of Numbers in Range II
LeetCode ID: 3753
Pattern: Math / Digit DP / Counting
Difficulty: Hard

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Precompute all 3-digit "wavy" patterns:
   - Middle digit is a peak:
       middle > left and middle > right
   - Or a valley:
       middle < left and middle < right
2. Define waveCount(N):
   - Counts total waviness contributed by all numbers <= N.
3. For each wavy pattern:
   - Count how many times it appears at every valid position.
4. Use:
       answer = waveCount(B) - waveCount(A - 1)
5. By linearity of counting, each valid peak/valley contributes
   independently to the final total.

Key Insight:
Instead of checking every number individually, count occurrences
of each wavy 3-digit pattern across all numbers up to N.
"""

class Solution:
    waves = []

    for i in range(1000):
        right = i % 10
        middle = (i // 10) % 10
        left = (i // 100) % 10

        if (middle > max(left, right)) or (middle < min(left, right)):
            waves.append(i)

    def totalWaviness(self, A: int, B: int) -> int:
        return self.waveCount(B) - self.waveCount(A - 1)

    def waveCount(self, num: int) -> int:
        if num < 100:
            return 0

        return sum(
            self.countWays(num, pattern)
            for pattern in self.waves
        )

    def countWays(self, num: int, pattern: int) -> int:
        s = str(num)
        n = len(s)

        leading_zero_pattern = pattern < 100
        count = 0

        for i in range(n - 2):
            prefix = int(s[:i] or 0)
            current = int(s[i:i + 3])
            suffix = int(s[i + 3:] or 0)

            multiplier = 10 ** (n - i - 3)

            ways = 0
            edge = 0

            if current > pattern:
                ways = prefix - leading_zero_pattern + 1

            elif current == pattern:
                ways = max(0, prefix - leading_zero_pattern)

                if prefix >= leading_zero_pattern:
                    edge = suffix + 1

            else:
                ways = max(0, prefix - leading_zero_pattern)

            count += ways * multiplier + edge

        return count