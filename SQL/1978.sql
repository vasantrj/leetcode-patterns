-- Problem: Employees Whose Manager Left the Company
-- LeetCode ID: 1978
-- Pattern: Subquery / Filtering
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Consider employees whose salary is less than 30000.
-- 2. Exclude employees who do not have a manager.
-- 3. Check whether their manager_id does not exist
--    in the Employees table.
-- 4. Return employee_id in ascending order.

SELECT
    employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id IS NOT NULL
  AND manager_id NOT IN (
        SELECT employee_id
        FROM Employees
  )
ORDER BY employee_id;
