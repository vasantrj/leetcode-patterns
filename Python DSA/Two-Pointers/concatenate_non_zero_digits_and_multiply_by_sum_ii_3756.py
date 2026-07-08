"""
Problem: Concatenate Non-Zero Digits and Multiply by Sum II
LeetCode ID: 3756
Pattern: Prefix Sum / Prefix Processing
Difficulty: Medium

Time Complexity: O(n + q)
Space Complexity: O(n)

where:
    n = length of the string
    q = number of queries

Approach:
1. Precompute three prefix arrays:
      - cnt[i] = number of non-zero digits in s[:i]
      - V[i] = concatenated value (mod MOD) of non-zero
               digits in s[:i]
      - S[i] = sum of digits in s[:i]
2. Precompute powers of 10 modulo MOD.
3. For each query:
      - Compute the digit sum using the prefix sum array.
      - Recover the concatenated non-zero number by
        removing the contribution of the prefix.
      - Return (number × digit_sum) % MOD.
"""

from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        digits = [int(c) for c in s]

        cnt = [0] * (n + 1)
        V = [0] * (n + 1)
        S = [0] * (n + 1)

        for i in range(n):
            d = digits[i]
            S[i + 1] = S[i] + d
            if d != 0:
                cnt[i + 1] = cnt[i] + 1
                V[i + 1] = (V[i] * 10 + d) % MOD
            else:
                cnt[i + 1] = cnt[i]
                V[i + 1] = V[i]

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []
        for l, r in queries:
            diff = cnt[r + 1] - cnt[l]
            X = (V[r + 1] - V[l] * pow10[diff]) % MOD
            total_sum = S[r + 1] - S[l]
            ans.append((X * total_sum) % MOD)

        return ans
        