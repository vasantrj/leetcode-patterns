"""
Problem: Process String with Special Operations I
LeetCode ID: 3612
Pattern: Strings / Simulation
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Traverse the string character by character.
2. Maintain the current result using a list.
3. Apply special operations:
      '*' -> Remove the last character.
      '#' -> Duplicate the current string.
      '%' -> Reverse the current string.
      letter -> Append to the result.
4. Convert the final list back to a string.
"""

class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for ch in s:
            if ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result.extend(result)
            elif ch == '%':
                result.reverse()
            else:
                result.append(ch)
        return ''.join(result)