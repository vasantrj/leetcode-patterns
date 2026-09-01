"""
Problem: Subarray Sum Equals K
LeetCode ID: 560
Pattern: Prefix Sum + HashMap
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Maintain a running prefix sum while iterating through the array.
2. If prefix_sum - k exists in the hashmap, it means a subarray with sum k exists.
3. Add the frequency of (prefix_sum - k) to the count.
4. Store/update the current prefix_sum in the hashmap.
5. Initialize hashmap with {0:1} to handle cases where subarray starts at index 0.
"""

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
        return count