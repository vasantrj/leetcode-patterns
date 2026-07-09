"""
Problem: Method Chaining
LeetCode ID: 2891
Pattern: Pandas / Method Chaining
Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Filter animals whose weight is greater than 100.
2. Sort the filtered rows by weight in descending order.
3. Select only the "name" column.
4. Perform all operations using method chaining.
"""

import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    return (
        animals
        .loc[animals["weight"] > 100]
        .sort_values("weight", ascending=False)
        [["name"]]
    )