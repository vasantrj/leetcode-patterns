-- Problem: Second Highest Salary
-- LeetCode ID: 176
-- Pattern: Subquery / DISTINCT
-- Difficulty: Medium
--
-- Time Complexity: O(n log n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Select distinct salaries to ignore duplicates.
-- 2. Sort salaries in descending order.
-- 3. Skip the highest salary using OFFSET 1.
-- 4. Return the next salary as the second highest.
-- 5. If no second highest salary exists, return NULL.

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
