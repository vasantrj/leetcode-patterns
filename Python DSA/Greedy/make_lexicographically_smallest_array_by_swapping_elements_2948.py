"""
Problem: Make Lexicographically Smallest Array by Swapping Elements
LeetCode ID: 2948
Pattern: Greedy / Sorting / Grouping
Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Sort the indices according to their values.
2. Group values together when consecutive sorted values differ
   by at most limit.
3. Elements belonging to the same group can be rearranged among
   their original positions.
4. Sort the original positions of each group.
5. Assign the group's sorted values to those positions in ascending
   order to obtain the lexicographically smallest result.
"""

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        id = sorted(range(n), key=lambda i: nums[i])
        result = [0] * n
        group_indices = [id[0]]
        group_values = [nums[id[0]]]

        for k in range(1, n):
            i = id[k]
            if nums[i] - nums[id[k-1]] <= limit:
                group_indices.append(i)
                group_values.append(nums[i])
            else:
                for pos, val in zip(sorted(group_indices), group_values):
                    result[pos] = val
                group_indices = [i]
                group_values = [nums[i]]

        for pos, val in zip(sorted(group_indices), group_values):
            result[pos] = val
        return result