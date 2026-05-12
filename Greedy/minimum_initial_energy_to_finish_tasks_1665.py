"""
Problem: Minimum Initial Energy to Finish Tasks
LeetCode ID: 1665
Pattern: Greedy / Sorting
Difficulty: Hard
Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Each task = [actual, minimum]
   - actual  = energy spent
   - minimum = minimum required energy before starting
2. Sort tasks by:
   (minimum - actual) descending
   so tasks with larger constraints are handled first.
3. Process tasks backwards:
   - Maintain minimum energy needed before current task.
4. Transition:
   energy = max(energy + actual, minimum)
5. Return minimum starting energy required.
"""

from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        energy = 0
        for actual, minimum in reversed(tasks):
            energy = max(energy + actual, minimum)
        return energy