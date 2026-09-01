"""
Problem: Smallest Subsequence of Distinct Characters
LeetCode ID: 1081
Pattern: Greedy / Monotonic Stack
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Record the last occurrence index of every character.
2. Traverse the string from left to right.
3. Skip characters already included in the subsequence.
4. While the current character is smaller than the top of the stack
   and the top character appears again later, remove the top character.
5. Push the current character onto the stack.
6. Join the stack to obtain the lexicographically smallest subsequence
   containing every distinct character exactly once.
"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue
            while stack and stack[-1] > c and i < last_occurrence[stack[-1]]:
                in_stack.discard(stack.pop())
            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)
    