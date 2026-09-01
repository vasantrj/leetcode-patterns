"""
Problem: Number of Recent Calls
LeetCode ID: 933
Pattern: Queue / Sliding Window
Difficulty: Easy

Time Complexity: O(n) amortized
Space Complexity: O(n)

Approach:
1. Store every ping timestamp in a queue.
2. For each new ping at time t, add it to the queue.
3. Remove timestamps that are older than t - 3000.
4. The remaining timestamps belong to the range:
      [t - 3000, t]
5. Return the number of timestamps currently in the queue.
"""

from collections import deque
class RecentCounter:
    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.popleft()
        return len(self.calls)