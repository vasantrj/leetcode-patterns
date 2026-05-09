"""
Problem: Minimum Jumps to Reach End via Prime Teleportation
LeetCode ID: 3629
Pattern: Graphs / BFS / Number Theory
Difficulty: Medium
Time Complexity: O(n log log M + n * sqrt(M))
Space Complexity: O(n + M)

Approach:
1. Use BFS since every move costs 1 jump.
2. From index i:
   - Move to i-1 or i+1
   - If nums[i] is prime p:
       teleport to every index j where nums[j] % p == 0
3. Precompute smallest prime factors (SPF) using sieve.
4. Build:
   prime_to_indices[p] = all indices whose values are divisible by p
5. During BFS:
   - Visit adjacent indices normally
   - Use teleportation only once per prime
     to avoid repeated processing.
6. Return minimum jumps to reach n-1.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        MAXV = max(nums)
        spf = list(range(MAXV + 1))

        for i in range(2, int(MAXV ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXV + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        prime_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            x = val
            seen = set()
            while x > 1:
                p = spf[x]
                if p not in seen:
                    prime_to_indices[p].append(idx)
                    seen.add(p)
                while x % p == 0:
                    x //= p

        queue = deque([(0, 0)])  # (index, jumps)
        visited = [False] * n
        visited[0] = True
        used_prime = set()

        while queue:
            i, dist = queue.popleft()
            if i == n - 1:
                return dist
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    queue.append((ni, dist + 1))

            val = nums[i]

            if val > 1 and spf[val] == val and val not in used_prime:
                used_prime.add(val)
                for ni in prime_to_indices[val]:
                    if not visited[ni]:
                        visited[ni] = True
                        queue.append((ni, dist + 1))

        return -1
    