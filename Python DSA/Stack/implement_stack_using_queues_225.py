"""
Problem: Implement Stack using Queues
LeetCode ID: 225
Pattern: Queue / Stack / Data Structure Design
Difficulty: Easy

Time Complexity:
    push()  -> O(n)
    pop()   -> O(1)
    top()   -> O(1)
    empty() -> O(1)

Space Complexity: O(n)

Approach:
1. Use a queue to store the stack elements.
2. When pushing a new element, append it to the queue.
3. Rotate all previous elements behind the new element.
4. This keeps the newest element at the front of the queue.
5. Therefore, pop() and top() can directly access the front.
"""

from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
