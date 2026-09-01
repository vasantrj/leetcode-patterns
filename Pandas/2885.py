"""
Problem: Rename Columns
LeetCode ID: 2885
Pattern: Pandas / DataFrame Operations
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Rename the "id" column to "student_id".
2. Use the DataFrame.rename() method.
3. Return the updated DataFrame.
"""

import pandas as pd
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id": "student_id", "first": "first_name", "last": "last_name","age": "age_in_years"})
