"""
Problem: Maximum Building Height
LeetCode ID: 1840
Pattern: Greedy / Constraint Propagation
Difficulty: Hard

Time Complexity: O(m log m)
Space Complexity: O(1)

Approach:
1. Add boundary restrictions:
      - Building 1 has height 0.
      - Building n can have height at most n - 1.
2. Sort restrictions by building id.
3. Forward pass:
      Propagate constraints from left to right.
4. Backward pass:
      Propagate constraints from right to left.
5. After both passes, all restrictions become
   consistent and as tight as possible.
6. For each adjacent restricted pair:
      (id1, h1) and (id2, h2)
   the maximum achievable peak between them is:

      (h1 + h2 + gap) // 2

7. Return the largest peak found.
"""

from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        
        # Forward pass: propagate constraints left to right
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
        
        # Backward pass: propagate constraints right to left
        for i in range(len(restrictions) - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
        
        ans = 0
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            # Max height between two restricted buildings
            # At some point between them, height can be (h1 + h2 + gap) // 2
            gap = id2 - id1
            peak = (h1 + h2 + gap) // 2
            ans = max(ans, peak)
        
        return ans
    


    