"""
Problem: Reshape Data: Melt
LeetCode ID: 2890
Pattern: Pandas / DataFrame Reshaping
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use the melt() method to unpivot the DataFrame.
2. Keep "student" as the identifier column.
3. Convert the subject columns into two new columns:
      - subject
      - score
4. Return the reshaped DataFrame.
"""

import pandas as pd
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=["product"],var_name="quarter",value_name="sales")

