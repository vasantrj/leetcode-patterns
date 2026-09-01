"""
Problem: Number of Days Between Two Dates
LeetCode ID: 1360
Pattern: Math / Date and Time
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Split each date into year, month, and day.
2. Convert both dates into Python date objects.
3. Subtract the two dates to get a timedelta.
4. Use .days to obtain the number of days.
5. Take the absolute value because the dates can be given
   in either order.
"""

from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        
        return abs((date(y1, m1, d1) - date(y2, m2, d2)).days)