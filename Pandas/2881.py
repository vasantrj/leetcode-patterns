"""
Problem: Create a New Column
LeetCode ID: 2881
Pattern: Pandas / Column Operations
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Create a new column named "bonus".
2. Set its value to twice the "salary" column.
3. Return the updated DataFrame.
"""

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees
