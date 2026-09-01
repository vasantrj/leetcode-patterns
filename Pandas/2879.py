"""
Problem: Display the First Three Rows
LeetCode ID: 2879
Pattern: Pandas / DataFrame Selection
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Use the DataFrame.head() method.
2. Pass 3 as the argument to retrieve the first
   three rows.
3. Return the resulting DataFrame.
"""

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
