"""
Problem: Find The Least Frequent Digit
LeetCode ID: 3663
Pattern: Mathematics / Frequency Counting
Difficulty: Easy

Time Complexity: O(d)
Space Complexity: O(1)

where:
    d = number of digits in n

Approach:
1. Convert n into a string to process each digit.
2. Count the frequency of every digit from 0 to 9.
3. Find the minimum non-zero frequency.
4. Traverse the digits from 0 to 9.
5. Return the smallest digit having that minimum frequency.
"""


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        
        # Count how many times each digit (0-9) appears
        counts = [0] * 10
        for ch in s:
            digit = int(ch)
            counts[digit] += 1
        
        # Find the smallest non-zero count (minimum frequency)
        min_count = float('inf')
        for c in counts:
            if c > 0 and c < min_count:
                min_count = c
        
        # Find the smallest digit that has this minimum frequency
        for digit in range(10):
            if counts[digit] == min_count:
                return digit
            