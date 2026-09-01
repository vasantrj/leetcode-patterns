"""
Problem: Robot Collisions
LeetCode ID: 2751
Pattern: Stack / Simulation / Sorting
Difficulty: Hard
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Each robot has:
   - position
   - health
   - direction
   - original index
2. Sort robots by position because collisions happen in positional order.
3. Use a stack to keep track of robots moving to the right ('R').
4. When a left-moving robot ('L') appears:
   - It may collide with robots in the stack.
   - Compare health values:
     a) If right robot health < left robot health:
        - Right robot dies
        - Left robot loses 1 health and continues
     b) If right robot health == left robot health:
        - Both die
     c) If right robot health > left robot health:
        - Left robot dies
        - Right robot loses 1 health
5. Surviving robots are collected and returned in original input order.
"""

from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])

        # Sort robots by position
        robots.sort()

        stack = []  # stores indices in robots list of alive right-moving robots

        for i in range(n):
            pos, health, direction, original_index = robots[i]

            if direction == 'R':
                stack.append(i)
            else:
                # direction == 'L'
                while stack and robots[i][1] > 0:
                    right_robot_index = stack[-1]

                    if robots[right_robot_index][1] < robots[i][1]:
                        # Right robot dies
                        robots[i][1] -= 1
                        robots[right_robot_index][1] = 0
                        stack.pop()

                    elif robots[right_robot_index][1] == robots[i][1]:
                        # Both die
                        robots[right_robot_index][1] = 0
                        robots[i][1] = 0
                        stack.pop()
                        break

                    else:
                        # Left robot dies
                        robots[right_robot_index][1] -= 1
                        robots[i][1] = 0
                        break

        # Collect surviving robots
        survivors = []
        for pos, health, direction, original_index in robots:
            if health > 0:
                survivors.append((original_index, health))

        survivors.sort()  # restore original order

        return [health for _, health in survivors]