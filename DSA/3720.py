"""
Problem: Lexicographically Smallest Permutation Greater Than Target
LeetCode ID: 3720
Pattern: Greedy / Frequency Counting / Lexicographical Order
Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n)

Approach:
1. Count the available characters in s.
2. Build a prefix that matches target as long as possible.
3. At every position, try to place the smallest available
   character greater than target[i].
4. If such a character exists, construct a candidate by
   placing it at the current position and putting all remaining
   characters in sorted order.
5. Continue matching target so that a candidate found at a
   later position has a smaller lexicographical value.
6. Return the last/best candidate found.
"""


from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(target)
        counts = Counter(s)        
        alphabet = sorted(set(s))       
        prefix = []     
        answer = ""  
        for i in range(n):
            t_char = target[i]
            for ch in alphabet:
                if ch > t_char and counts[ch] > 0:
                    counts[ch] -= 1
                    rest = []
                    for c in alphabet:
                        rest.extend([c] * counts[c])
                    answer = ''.join(prefix) + ch + ''.join(rest)
                    counts[ch] += 1   
                    break             

            if counts[t_char] > 0:
                counts[t_char] -= 1
                prefix.append(t_char)
            else:
                break
        return answer