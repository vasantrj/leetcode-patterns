"""
Problem: Remove Duplicates from Sorted List
LeetCode ID: 83
Pattern: Linked List / Two Pointers
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the linked list using a current pointer.
2. Since the list is sorted, duplicate values appear next
   to each other.
3. If the current node and next node have the same value,
   skip the next node.
4. Otherwise, move the pointer forward.
5. Return the original head.
"""

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

        