class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        
        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Calculate maximum twin sum
        max_sum = 0
        first = head
        second = prev
        
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum