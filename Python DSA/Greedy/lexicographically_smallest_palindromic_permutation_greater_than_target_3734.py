"""
Problem: Lexicographically Smallest Palindromic Permutation Greater Than Target
LeetCode ID: 3734
Pattern: Greedy / Frequency Counting / Palindrome
Difficulty: Hard

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Count the frequency of every character.
2. Check whether a palindrome can be formed:
      - Even length -> every character must have an even frequency.
      - Odd length  -> exactly one character must have an odd frequency.
3. Since a palindrome is completely determined by its first half
   and its middle character, work only with the first half.
4. Try to keep the first half equal to the target for as long as possible.
5. If necessary, move from right to left and increase the character
   at the latest possible position.
6. Fill the remaining positions with the smallest available characters.
7. Construct the complete palindrome from the selected first half.
"""

from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c in cnt if cnt[c] % 2 == 1]
        
        if n % 2 == 0:
            if odd_chars:
                return ""
            mid_char = None
        else:
            if len(odd_chars) != 1:
                return ""
            mid_char = odd_chars[0]
        
        half_pool = {chr(ord('a') + k): cnt.get(chr(ord('a') + k), 0) // 2 for k in range(26)}
        h = n // 2
        
        def build_full(A_list):
            A_str = ''.join(A_list)
            if n % 2 == 0:
                return A_str + A_str[::-1]
            else:
                return A_str + mid_char + A_str[::-1]
        
        # Determine max tight-matchable prefix length L
        running = {chr(ord('a') + k): 0 for k in range(26)}
        L = h
        for i in range(h):
            ch = target[i]
            if running[ch] < half_pool[ch]:
                running[ch] += 1
            else:
                L = i
                break
        
        start_pos = None
        if L == h:
            A_full = list(target[:h])
            if n % 2 == 0:
                second_half = A_full[::-1]
                if ''.join(second_half) > target[h:]:
                    return build_full(A_full)
            else:
                if mid_char > target[h]:
                    return build_full(A_full)
                elif mid_char == target[h]:
                    second_half = ''.join(A_full[::-1])
                    if second_half > target[h + 1:]:
                        return build_full(A_full)
            start_pos = h - 1
        else:
            start_pos = L
        
        if start_pos < 0:
            return ""
        
        used_counts = {chr(ord('a') + k): 0 for k in range(26)}
        for k in range(start_pos):
            used_counts[target[k]] += 1
        
        for i in range(start_pos, -1, -1):
            ch_target = target[i]
            found = None
            for code in range(ord(ch_target) + 1, ord('z') + 1):
                c = chr(code)
                if half_pool[c] - used_counts[c] > 0:
                    found = c
                    break
            if found:
                remaining = {c: half_pool[c] - used_counts[c] for c in half_pool}
                remaining[found] -= 1
                fill = []
                for k in range(26):
                    c = chr(ord('a') + k)
                    fill.extend([c] * remaining[c])
                A = list(target[:i]) + [found] + fill
                return build_full(A)
            if i > 0:
                used_counts[target[i - 1]] -= 1
        
        return ""