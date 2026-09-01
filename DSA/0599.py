"""
Problem: Minimum Index Sum of Two Lists
LeetCode ID: 599
Pattern: Hash Map / Arrays
Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n)

Approach:
1. Store the index of every restaurant in list1 using a hash map.
2. Traverse list2 and check whether each restaurant exists in list1.
3. Calculate the sum of the two indices.
4. Keep track of the minimum index sum.
5. If another restaurant has the same minimum sum, add it
   to the result.
"""

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {name: i for i, name in enumerate(list1)}
        best_sum = float('inf')
        result = []
        for j, name in enumerate(list2):
            if name in index1:
                total = index1[name] + j
                if total < best_sum:
                    best_sum = total
                    result = [name]
                elif total == best_sum:
                    result.append(name)
        
        return result
