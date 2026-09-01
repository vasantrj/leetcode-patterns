"""
Problem: Cinema Seat Allocation
LeetCode ID: 1386
Pattern: Bit Manipulation / Bitmask
Difficulty: Medium

Time Complexity: O(m)
Space Complexity: O(m)

where:
    m = number of reserved seats

Approach:
1. Only seats 2 through 9 can affect the placement of a
   four-person family.
2. Represent the reserved seats of each affected row using
   a bitmask.
3. There are three possible blocks for a family:
      - Left:  seats 2-5
      - Middle: seats 4-7
      - Right: seats 6-9
4. Rows without any relevant reserved seats can always fit
   two families.
5. For each affected row:
      - If both left and right blocks are available → 2 families.
      - If either left or right is available → 1 family.
      - Otherwise, check the middle block.
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                row_masks[row] |= (1 << seat)

        LEFT  = 0b0000111100   # seats 2,3,4,5
        MID   = 0b0011110000   # seats 4,5,6,7
        RIGHT = 0b1111000000   # seats 6,7,8,9
        total = 2 * (n - len(row_masks))
        for mask in row_masks.values():
            can_left = (mask & LEFT) == 0
            can_right = (mask & RIGHT) == 0
            if can_left and can_right:
                total += 2
            elif can_left or can_right:
                total += 1
            else:
                can_mid = (mask & MID) == 0
                if can_mid:
                    total += 1
        return total