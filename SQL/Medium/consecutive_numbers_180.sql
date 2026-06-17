-- Problem: Consecutive Numbers
-- LeetCode ID: 180
-- Pattern: SELF JOIN
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Logs table three times.
-- 2. Check three consecutive ids:
--      l1.id = l2.id - 1
--      l2.id = l3.id - 1
-- 3. Ensure all three numbers are equal.
-- 4. Return distinct numbers that appear
--    at least three times consecutively.

SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2
    ON l1.id = l2.id - 1
JOIN Logs l3
    ON l2.id = l3.id - 1
WHERE l1.num = l2.num
  AND l2.num = l3.num;