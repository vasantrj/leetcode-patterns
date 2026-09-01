-- Problem: Rising Temperature
-- LeetCode ID: 197
-- Pattern: SELF JOIN
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Weather table with itself.
-- 2. Match records where the date difference is exactly 1 day.
-- 3. Keep rows where today's temperature is higher than yesterday's.
-- 4. Return today's id.

SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;