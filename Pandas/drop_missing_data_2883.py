"""
Problem: Drop Missing Data
LeetCode ID: 2883
Pattern: Pandas / Data Cleaning
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Remove rows where the "name" column contains
   missing (NaN) values.
2. Keep all remaining rows unchanged.
3. Return the cleaned DataFrame.
"""

import pandas as pd
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
