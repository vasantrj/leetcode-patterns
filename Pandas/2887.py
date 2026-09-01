"""
Problem: Fill Missing Data
LeetCode ID: 2887
Pattern: Pandas / Missing Data Handling
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Replace missing (NaN) values in the "quantity" column with 0.
2. Use the fillna() method.
3. Return the updated DataFrame.
"""

import pandas as pd
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products
