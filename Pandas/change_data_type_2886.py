"""
Problem: Change Data Type
LeetCode ID: 2886
Pattern: Pandas / Data Type Conversion
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Convert the "grade" column to integer type.
2. Use the astype() method for type conversion.
3. Return the updated DataFrame.
"""

import pandas as pd
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students
