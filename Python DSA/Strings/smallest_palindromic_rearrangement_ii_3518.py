"""
Problem: Smallest Palindromic Rearrangement II
LeetCode ID: 3518
Pattern: Strings / Greedy / Combinatorics
Difficulty: Hard

Time Complexity: O(n + m × k)
Space Complexity: O(k)

where:
    n = length of the string
    m = length of the palindrome's left half
    k = number of distinct characters

Approach:
1. Count the frequency of every character.
2. Extract the middle character (if any) and compute
   the frequency of each character in the left half.
3. Calculate the total number of distinct permutations
   of the left half using multinomial coefficients.
4. If k exceeds the total number of valid permutations,
   return an empty string.
5. Build the left half greedily:
      - Try each available character in lexicographical order.
      - Compute how many permutations start with it.
      - If the desired k-th palindrome lies in that range,
        choose it; otherwise, skip those permutations.
6. Mirror the left half around the middle character.
"""

import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        mid = ''
        half_counts = {}
        for c, f in freq.items():
            if f % 2 == 1:
                mid = c
            half_counts[c] = f // 2

        m = sum(half_counts.values())
        chars = sorted(half_counts.keys())
        cnt_list = [half_counts[c] for c in chars]
        P = math.factorial(m)
        for cnt in cnt_list:
            P //= math.factorial(cnt)

        if k > P:
            return ""

        remaining_total = m
        result = []
        for _ in range(m):
            for i, c in enumerate(chars):
                if cnt_list[i] == 0:
                    continue
                sub = P * cnt_list[i] // remaining_total
                if k <= sub:
                    result.append(c)
                    cnt_list[i] -= 1
                    remaining_total -= 1
                    P = sub
                    break
                else:
                    k -= sub

        half = ''.join(result)
        if mid:
            return half + mid + half[::-1]
        else:
            return half + half[::-1]
            