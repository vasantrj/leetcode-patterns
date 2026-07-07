"""
Problem: Modify Columns
LeetCode ID: 2884
Pattern: Pandas / Column Operations
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Multiply every value in the "salary" column by 2.
2. Update the existing "salary" column.
3. Return the modified DataFrame.
"""

import pandas as pd
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] *= 2
    return employees

