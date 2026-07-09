"""
Problem: Reshape Data: Pivot
LeetCode ID: 2889
Pattern: Pandas / DataFrame Reshaping
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use the pivot() method to reshape the DataFrame.
2. Use "month" as the index.
3. Use "city" as the columns.
4. Use "temperature" as the values.
5. Return the pivoted DataFrame.
"""

import pandas as pd
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month",columns="city",values="temperature")

