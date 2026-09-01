"""
Problem: Number of ZigZag Arrays II
LeetCode ID: 3700
Pattern: Dynamic Programming / Matrix Exponentiation
Difficulty: Hard

Time Complexity: O((2m)^3 * log n)
Space Complexity: O((2m)^2)

where:
    m = r - l + 1

Approach:
1. Represent each state as:
      (value, direction)

   direction:
      0 -> arrived going up
      1 -> arrived going down

2. Build a transition matrix T:
      - From an UP state, next value must be smaller.
      - From a DOWN state, next value must be larger.

3. Since n can be as large as 10^9,
   use matrix exponentiation to compute:

      T^(n - 1)

4. Multiply the resulting matrix by the initial state vector.

5. Sum all final states modulo 1e9 + 7.
"""

from typing import List

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        size = m * 2 
        
        def mat_mul(A, B):
            sz = len(A)
            C = [[0]*sz for _ in range(sz)]
            for i in range(sz):
                for k in range(sz):
                    if A[i][k] == 0: continue
                    for j in range(sz):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
        
        def mat_pow(M, p):
            sz = len(M)
            result = [[1 if i==j else 0 for j in range(sz)] for i in range(sz)]
            while p:
                if p & 1: result = mat_mul(result, M)
                M = mat_mul(M, M)
                p >>= 1
            return result
        
        T = [[0]*size for _ in range(size)]
        for v in range(m):
            for u in range(v):  
                T[u*2+1][v*2+0] = 1
            for u in range(v+1, m): 
                T[u*2+0][v*2+1] = 1
        
        vec = [1] * size
        Tp = mat_pow(T, n-1)  
        ans = 0
        for j in range(size):
            col_sum = sum(Tp[i][j] * vec[j] for i in range(size)) % MOD
            ans = (ans + col_sum) % MOD
        res = [0]*size
        for i in range(size):
            for j in range(size):
                res[i] = (res[i] + Tp[i][j] * vec[j]) % MOD
        
        return sum(res) % MOD

        