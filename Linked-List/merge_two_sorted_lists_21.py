"""
Problem: Merge Two Sorted Lists
LeetCode ID: 21
Pattern: Linked List / Two Pointers
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(1)

Approach:
1. Use a dummy node to simplify list construction.
2. Compare current nodes of both lists:
   - Attach smaller node to merged list
   - Move corresponding pointer forward
3. Continue until one list becomes empty.
4. Attach remaining nodes from the non-empty list.
5. Return dummy.next as merged head.
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self,list1: Optional['ListNode'],list2: Optional['ListNode']) -> Optional['ListNode']:

        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return dummy.next
    