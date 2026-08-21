"""
Problem: Reverse Linked List
LeetCode ID: 206
Pattern: Linked List / Iteration
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain three pointers:
      - prev: previous node
      - curr: current node
      - next_node: next node
2. Save the next node before changing curr.next.
3. Reverse the current node's pointer.
4. Move prev and curr one step forward.
5. When curr becomes None, prev is the new head.
"""

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev