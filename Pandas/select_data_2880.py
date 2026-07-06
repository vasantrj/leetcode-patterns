"""
Problem: Select Data
LeetCode ID: 2880
Pattern: Pandas / DataFrame Selection
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Filter the DataFrame to keep only the row
   where student_id equals 101.
2. Select only the "name" and "age" columns.
3. Return the filtered DataFrame.
"""

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101,["name", "age"]]
