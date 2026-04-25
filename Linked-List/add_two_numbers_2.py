"""
Problem: Add Two Numbers
LeetCode ID: 2
Pattern: Linked List
Difficulty: Medium
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

Approach:
1. The linked lists store digits in reverse order.
2. Traverse both lists simultaneously.
3. At each step:
   - Take current digit from l1 and l2 (0 if absent)
   - Add carry from previous step
4. Create a new node with digit = total % 10
5. Update carry = total // 10
6. Continue until both lists and carry are exhausted.
7. Return dummy.next as the result head.
"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next