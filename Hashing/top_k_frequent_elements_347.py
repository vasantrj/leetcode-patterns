"""
Problem: Top K Frequent Elements
LeetCode ID: 347
Pattern: Hashing + Bucket Sort / Heap
Difficulty: Medium

Approach 1: Bucket Sort
Time Complexity: O(n)
Space Complexity: O(n)

Approach 2: Min Heap
Time Complexity: O(n log k)
Space Complexity: O(n)
"""

from typing import List
import heapq

class Solution:
    # Approach 1: Bucket Sort (Optimal)
    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        # Step 1: Frequency count
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        # Step 2: Buckets
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        # Step 3: Collect top k
        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

    # Approach 2: Min Heap
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        # Step 1: Frequency count
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        # Step 2: Min heap of size k
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
    