"""
Problem: Drop Duplicate Rows
LeetCode ID: 2882
Pattern: Pandas / Data Cleaning
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Remove duplicate rows based on the "email" column.
2. Keep the first occurrence of each email.
3. Return the cleaned DataFrame.
"""

import pandas as pd
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"],keep="first")
