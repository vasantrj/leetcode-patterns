"""
Problem: Walking Robot Simulation II
LeetCode ID: 2069
Pattern: Simulation / Design
Difficulty: Medium
Time Complexity: O(1) per operation
Space Complexity: O(1)

Approach:
1. The robot moves only along the boundary of the rectangle.
2. Total perimeter cells covered in one full cycle:
   perimeter = 2 * (width + height - 2)
3. Instead of simulating each step one by one:
   - Keep track of current perimeter position using modulo arithmetic.
4. Use:
   - self.pos   -> current position on the perimeter path
   - self.moved -> whether robot has moved at least once
5. getPos():
   - Convert perimeter index into (x, y) coordinates.
6. getDir():
   - Determine direction based on current perimeter segment.
   - Special case:
     - Before any move at origin -> "East"
     - After full cycle back to origin -> "South"
"""

class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height - 2)
        self.pos = 0
        self.moved = False  # Track if any step was taken

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        w, h, p = self.w, self.h, self.pos
        if p < w:
            return [p, 0]
        p -= w - 1
        if p < h:
            return [w - 1, p]
        p -= h - 1
        if p < w:
            return [w - 1 - p, h - 1]
        p -= w - 1
        return [0, h - 1 - p]

    def getDir(self) -> str:
        if not self.moved:
            return "East"   # Initial state
        w, h, p = self.w, self.h, self.pos
        if p == 0:          # Back at origin after movement = came from South
            return "South"
        if p < w:
            return "East"
        if p < w + h - 1:
            return "North"
        if p < 2 * w + h - 2:
            return "West"
        return "South"
    