"""
Problem: Walking Robot Simulation
LeetCode ID: 874
Pattern: Hashing / Simulation
Difficulty: Medium
Time Complexity: O(n + m)
Space Complexity: O(m)

Approach:
1. The robot starts at (0, 0) facing north.
2. Commands:
   - -2 -> turn left 90 degrees
   - -1 -> turn right 90 degrees
   - positive number -> move forward step by step
3. Store all obstacles in a set for O(1) lookup.
4. For each movement command:
   - Move one step at a time.
   - Stop early if the next cell is an obstacle.
5. Track the maximum Euclidean distance squared from origin.
"""

from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        # North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0
        x = y = 0
        max_distance = 0
        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = directions[direction_index]
                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                    max_distance = max(max_distance, x * x + y * y)
        return max_distance