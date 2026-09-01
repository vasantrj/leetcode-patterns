"""
Problem: Implement Queue using Stacks
LeetCode ID: 232
Pattern: Stack / Queue / Data Structure Design
Difficulty: Easy

Time Complexity:
    push()  -> O(1)
    pop()   -> O(1) amortized
    peek()  -> O(1) amortized
    empty() -> O(1)

Space Complexity: O(n)

Approach:
1. Use two stacks:
      - in_stack  -> stores newly added elements.
      - out_stack -> provides elements in queue order.
2. push() simply adds the element to in_stack.
3. Before pop() or peek(), transfer elements from in_stack
   to out_stack only when out_stack is empty.
4. Reversing the order during transfer makes the oldest
   element available at the top of out_stack.
5. Keep using out_stack until it becomes empty.
"""


class MyQueue:
    def __init__(self):
        self.in_stack = [] 
        self.out_stack = [] 

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def _transfer_if_needed(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())