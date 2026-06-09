-- Problem: Employee Bonus
-- LeetCode ID: 577
-- Pattern: LEFT JOIN / Filtering
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Employee and Bonus tables using empId.
-- 2. Use LEFT JOIN to include employees without a bonus.
-- 3. Keep employees whose bonus is:
--      - less than 1000
--      - OR NULL
-- 4. Return employee name and bonus.

SELECT
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus < 1000
   OR b.bonus IS NULL;