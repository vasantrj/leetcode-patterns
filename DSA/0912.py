"""
Problem: Sort an Array
LeetCode ID: 912
Pattern: Sorting / Merge Sort
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. We need to sort the given array in ascending order.
2. Use Merge Sort:
   - Divide the array into two halves recursively.
   - Sort both halves.
   - Merge them back in sorted order.
3. Merge Sort guarantees O(n log n) time complexity.
4. It is stable and works efficiently for large inputs.
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        def merge(left: List[int], right: List[int]) -> List[int]:
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        return merge_sort(nums)
    