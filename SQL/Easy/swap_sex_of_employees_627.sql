/*
Problem: Swap Sex of Employees
LeetCode ID: 627
Pattern: SQL / UPDATE / Conditional Function
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Update every row in the salary table.
2. Use the IF() function to swap:
      - 'm' → 'f'
      - 'f' → 'm'
3. The update is performed in a single SQL statement.
*/

UPDATE Salary
SET sex = IF(sex = 'm', 'f', 'm');