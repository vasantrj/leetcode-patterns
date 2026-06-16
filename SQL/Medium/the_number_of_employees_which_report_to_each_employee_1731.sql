-- Problem: The Number of Employees Which Report to Each Employee
-- LeetCode ID: 1731
-- Pattern: SELF JOIN / GROUP BY
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Self-join Employees table:
--      manager.employee_id = employee.reports_to
-- 2. Count direct reports for each manager.
-- 3. Compute average age of reporting employees.
-- 4. Round average age to the nearest integer.
-- 5. Return employee_id, name, reports_count, and average_age.

SELECT
    m.employee_id,
    m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM Employees m
JOIN Employees e
    ON m.employee_id = e.reports_to
GROUP BY
    m.employee_id,
    m.name
ORDER BY m.employee_id;