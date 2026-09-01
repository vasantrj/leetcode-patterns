"""
Problem: Excel Sheet Column Title
LeetCode ID: 168
Pattern: Mathematics / Base Conversion
Difficulty: Easy

Time Complexity: O(log26(n))
Space Complexity: O(log26(n))

Approach:
1. Excel columns use a 1-indexed base-26 system.
2. Repeatedly subtract 1 to convert it into a 0-indexed system.
3. Compute the current character using modulo 26.
4. Append the corresponding uppercase letter.
5. Divide the number by 26 and repeat.
6. Reverse the collected characters to obtain the final title.
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))