"""
Problem: Valid Parentheses
LeetCode ID: 20
Pattern: Stack
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a stack to track opening brackets.
2. Traverse each character:
   - If opening bracket -> push onto stack
   - If closing bracket:
       check whether stack top matches corresponding opening bracket
3. If mismatch or stack empty -> invalid.
4. At the end:
   - valid only if stack is empty.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0