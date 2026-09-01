"""
Problem: Palindrome Linked List
LeetCode ID: 234
Pattern: Linked List / Fast & Slow Pointers / Reversal
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use slow and fast pointers to find the middle of the list.
2. Reverse the second half of the linked list.
3. Compare the first half with the reversed second half.
4. If every corresponding value matches, the list is a palindrome.
"""

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        left, right = head, prev
        result = True
        while right:
            if left.val != right.val:
                result = False
                break
            left = left.next
            right = right.next
        return result

    