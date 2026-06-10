-- Problem: Project Employees I
-- LeetCode ID: 1075
-- Pattern: JOIN / GROUP BY / AVG
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Project and Employee tables using employee_id.
-- 2. Group records by project_id.
-- 3. Calculate the average experience years of employees
--    working on each project.
-- 4. Round the result to 2 decimal places.

SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id;