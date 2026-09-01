"""
Problem: Process String with Special Operations II
LeetCode ID: 3614
Pattern: Strings / Simulation / Reverse Processing
Difficulty: Hard

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Building the final string is impossible because its
   length can grow up to 10^15.
2. First pass:
      - Compute the length of the resulting string after
        each operation.
      - Store these lengths in an array.
3. If k is outside the final string length:
      return '.'
4. Second pass (reverse):
      - Trace position k backwards through the operations.
      - Undo each operation:
          '*' -> deletion
          '#' -> duplication
          '%' -> reversal
          letter -> appended character
5. When the traced position corresponds to an appended
   character, return that character.
"""

class Solution:
    def processStr(self, s: str, k: int) -> str:

        lengths = [0] * (len(s) + 1)

        for i, c in enumerate(s):
            current_length = lengths[i]

            if c == '*':
                lengths[i + 1] = max(0, current_length - 1)

            elif c == '#':
                lengths[i + 1] = current_length * 2

            elif c == '%':
                lengths[i + 1] = current_length

            else:
                lengths[i + 1] = current_length + 1

        if k >= lengths[len(s)]:
            return '.'

        pos = k

        for i in range(len(s) - 1, -1, -1):

            c = s[i]

            prev_len = lengths[i]
            cur_len = lengths[i + 1]

            if c == '*':
                pass

            elif c == '#':
                if pos >= prev_len:
                    pos -= prev_len

            elif c == '%':
                pos = cur_len - 1 - pos

            else:
                if pos == prev_len:
                    return c

        return '.'