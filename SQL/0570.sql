-- Problem: Managers with at Least 5 Direct Reports
-- LeetCode ID: 570
-- Pattern: SELF JOIN / GROUP BY
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Employees report to managers via managerId.
-- 2. Group employees by managerId.
-- 3. Keep managers having at least 5 direct reports.
-- 4. Join back with Employee table to get manager names.

SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) m
ON e.id = m.managerId;