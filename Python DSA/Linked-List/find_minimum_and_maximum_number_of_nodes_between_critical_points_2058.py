"""
Problem: Find the Minimum and Maximum Number of Nodes Between Critical Points
LeetCode ID: 2058
Pattern: Linked List / Traversal
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the linked list while keeping track of the previous,
   current, and next nodes.
2. A node is a critical point if it is either:
      - A local maximum.
      - A local minimum.
3. Track:
      - first_idx: index of the first critical point.
      - prev_idx: index of the most recent critical point.
      - min_dist: minimum distance between consecutive critical points.
4. The maximum distance is between the first and last critical points.
5. Return [-1, -1] if fewer than two critical points exist.
"""

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        idx = 1  # index of cur
        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')
        
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
            
            prev = curr
            curr = curr.next
            idx += 1
        
        if first_idx == -1 or prev_idx == first_idx:
            return [-1, -1]
        
        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]