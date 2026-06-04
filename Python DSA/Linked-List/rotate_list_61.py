"""
Problem: Rotate List
LeetCode ID: 61
Pattern: Linked List / Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. If list is empty or has one node → return head.
2. Compute length of list.
3. Connect tail to head to form a circular list.
4. Effective rotations = k % length.
5. Find new tail:
   - Move (length - k % length - 1) steps from head.
6. New head = new_tail.next
7. Break the cycle.
8. Return new head.
"""

from typing import Optional

class Solution:
    def rotateRight(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        tail.next = head

        k = k % length
        steps = length - k - 1

        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
    