"""
Problem: Reshape Data: Concatenate
LeetCode ID: 2888
Pattern: Pandas / DataFrame Reshaping
Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n + m)

where:
    n = number of rows in df1
    m = number of rows in df2

Approach:
1. Concatenate the two DataFrames vertically.
2. Ignore the original indices and create a new
   continuous index.
3. Return the combined DataFrame.
"""

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2],ignore_index=True)
    