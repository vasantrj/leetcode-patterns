-- Problem: Department Top Three Salaries
-- LeetCode ID: 185
-- Pattern: Window Function / DENSE_RANK
-- Difficulty: Hard
--
-- Time Complexity: O(n log n)
-- Space Complexity: O(n)
--
-- Approach:
-- 1. Join Employee and Department tables.
-- 2. For each department, rank salaries using DENSE_RANK()
--    in descending order.
-- 3. Keep employees whose salary rank is within the top 3.
-- 4. Return the department name, employee name, and salary.

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
) ranked
WHERE salary_rank <= 3;

