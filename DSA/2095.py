"""
Problem: Delete the Middle Node of a Linked List
LeetCode ID: 2095
Pattern: Linked List / Fast & Slow Pointers
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Handle the edge case where the list contains only one node.
2. Use slow and fast pointers to find the middle node:
      - slow moves one step
      - fast moves two steps
3. Keep track of the node before slow using prev.
4. Once slow reaches the middle:
      prev.next = slow.next
5. Return the modified list.
"""

from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head