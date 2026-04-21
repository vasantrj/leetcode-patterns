"""
Problem: Minimize Hamming Distance After Swap Operations
LeetCode ID: 1722
Pattern: Graphs / Union Find / Hashing
Difficulty: Medium
Time Complexity: O(n α(n))
Space Complexity: O(n)

Approach:
1. Indices connected through allowed swaps form components.
2. Any values inside the same component can be rearranged freely.
3. Use Union-Find (DSU) to group connected indices.
4. For each component:
   - Count source values using Counter.
   - Try matching target values greedily.
5. If a target value is unavailable, it contributes to Hamming distance.
6. Sum unmatched positions across all components.
"""

from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]]
    ) -> int:
        n = len(source)

        # Union-Find
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            parent[find(a)] = find(b)

        for a, b in allowedSwaps:
            union(a, b)

        # Group indices by component
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        # Compute minimum Hamming distance
        hamming = 0

        for indices in groups.values():
            src_count = Counter(source[i] for i in indices)

            for i in indices:
                t = target[i]
                if src_count[t] > 0:
                    src_count[t] -= 1
                else:
                    hamming += 1

        return hamming