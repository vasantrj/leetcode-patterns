"""
Problem: Calculate Special Bonus
LeetCode ID: 1873
Pattern: Pandas / Conditional Selection
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Create a new "bonus" column initialized to 0.
2. Find employees whose:
      - employee_id is odd, and
      - name does not start with 'M'.
3. Set their bonus equal to their salary.
4. Return the required columns sorted by employee_id.
"""

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0
    mask = ((employees["employee_id"] % 2 == 1) & (~employees["name"].str.startswith("M")))
    employees.loc[mask, "bonus"] = employees.loc[mask, "salary"]
    return employees[["employee_id", "bonus"]].sort_values("employee_id")
