"""
Problem: Furthest Point From Origin
LeetCode ID: 2833
Pattern: Strings / Counting
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Count:
   - 'L' moves
   - 'R' moves
   - '_' blank moves
2. Fixed displacement after known moves:
   abs(R - L)
3. Each blank move can be assigned optimally to extend the dominant side.
4. Therefore:
   answer = abs(R - L) + blanks
"""

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = moves.count('L')
        R = moves.count('R')
        blanks = moves.count('_')

        return abs(R - L) + blanks
    
    