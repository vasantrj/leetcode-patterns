"""
Problem: Lexicographically Smallest Generated String
LeetCode ID: 3474
Pattern: Greedy / Strings
Difficulty: Medium
Time Complexity: O(n * m)
Space Complexity: O(n)

Approach:
1. We need to build the lexicographically smallest valid string.
2. For each position:
   - If str1[i] == 'T', then word2 MUST start at index i.
   - If str1[i] == 'F', then word2 MUST NOT start at index i.
3. First, place all mandatory matches for 'T':
   - Copy word2 into result at every required starting position.
   - If conflicting characters appear, return "".
4. Fill all remaining empty positions with 'a' to make the string lexicographically smallest.
5. Check all 'F' positions:
   - If word2 matches exactly at any forbidden position, modify the earliest possible free character
     in that window with the smallest valid character to break the match.
   - If impossible, return "".
6. Return the final string.
"""

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        result_len = n + m - 1
        result = ['?'] * result_len
        fixed = [False] * result_len
        # Step 1: Force all 'T' matches
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if result[pos] == '?':
                        result[pos] = str2[j]
                        fixed[pos] = True
                    elif result[pos] != str2[j]:
                        return ""
        # Step 2: Fill remaining with 'a'
        for i in range(result_len):
            if result[i] == '?':
                result[i] = 'a'
        # Step 3: Break all forbidden 'F' matches
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(result[i:i + m]) == str2:
                    changed = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not fixed[pos]:
                            original = result[pos]
                            for ch in "abcdefghijklmnopqrstuvwxyz":
                                if ch != original:
                                    result[pos] = ch
                                    changed = True
                                    break
                            if changed:
                                break
                    if not changed:
                        return ""
        return ''.join(result)