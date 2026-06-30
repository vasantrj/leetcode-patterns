"""
Problem: Get the Size of a DataFrame
LeetCode ID: 2878
Pattern: Pandas / DataFrame Properties
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Use the DataFrame.shape attribute to get:
      - Number of rows
      - Number of columns
2. Return the result as a list:
      [rows, columns]
"""

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list:
    return list(players.shape)
