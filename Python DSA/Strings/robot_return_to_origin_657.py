"""
Problem: Robot Return to Origin
LeetCode ID: 657
Pattern: Strings / Simulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Start from origin (0, 0).
2. Traverse each move in the string:
   - 'U' -> move up
   - 'D' -> move down
   - 'L' -> move left
   - 'R' -> move right
3. After processing all moves:
   - If final position is (0, 0), return True
   - Otherwise, return False
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0

        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            else:  # move == 'R'
                x += 1

        return x == 0 and y == 0