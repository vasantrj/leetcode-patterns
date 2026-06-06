-- Problem: Replace Employee ID With The Unique Identifier
-- LeetCode ID: 1378
-- Pattern: LEFT JOIN
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Employees with EmployeeUNI using employee id.
-- 2. Use LEFT JOIN to keep all employees.
-- 3. Return unique_id and employee name.
-- 4. If no matching unique_id exists, return NULL.

SELECT
    eu.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id;