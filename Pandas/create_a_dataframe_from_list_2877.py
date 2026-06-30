"""
Problem: Create a DataFrame from List
LeetCode ID: 2877
Pattern: Pandas / DataFrame Creation
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Convert the input list into a pandas DataFrame.
2. Assign the column names:
      - student_id
      - age
3. Return the DataFrame.
"""

import pandas as pd


def createDataframe(student_data):
    return pd.DataFrame(
        student_data,
        columns=["student_id", "age"]
    )
