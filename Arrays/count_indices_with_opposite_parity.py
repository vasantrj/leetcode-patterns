"""
Problem: Count Indices With Opposite Parity
Pattern: Arrays / Prefix-Suffix Counting
Difficulty: Easy-Medium
Time Complexity: O(n)
Space Complexity: O(1) extra (excluding output)

Approach:
1. Traverse the array from right to left.
2. Maintain:
   - even_count = number of even elements to the right
   - odd_count  = number of odd elements to the right
3. For each index:
   - If current number is even → count opposite = odd_count
   - If current number is odd  → count opposite = even_count
4. Update counts accordingly.
5. Return the result array.
"""

from typing import List

class Solution:
    def countOppositeParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        even_count = 0
        odd_count = 0
        for i in range(n - 1, -1, -1):
            if nums[i] % 2 == 0:
                answer[i] = odd_count
                even_count += 1
            else:
                answer[i] = even_count
                odd_count += 1
        return answer