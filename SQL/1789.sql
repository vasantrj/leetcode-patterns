-- Problem: Primary Department for Each Employee
-- LeetCode ID: 1789
-- Pattern: Filtering / UNION
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Employees with only one department automatically
--    have that department as their primary department.
-- 2. Employees with multiple departments have exactly
--    one row where primary_flag = 'Y'.
-- 3. Combine both cases using OR filtering.

SELECT
    employee_id,
    department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id IN (
        SELECT employee_id
        FROM Employee
        GROUP BY employee_id
        HAVING COUNT(*) = 1
   );