"""
Problem: Remove Linked List Elements
LeetCode ID: 203
Pattern: Linked List / Dummy Node
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Create a dummy node before the head to handle cases
   where the head itself needs to be removed.
2. Use two pointers:
      - prev: previous node
      - curr: current node
3. If curr.val equals the target value, skip the current node.
4. Otherwise, move prev forward.
5. Continue until the entire list is processed.
6. Return dummy.next as the new head.
"""

from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
