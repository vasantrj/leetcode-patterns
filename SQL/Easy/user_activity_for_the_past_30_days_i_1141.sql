-- Problem: User Activity for the Past 30 Days I
-- LeetCode ID: 1141
-- Pattern: GROUP BY / COUNT DISTINCT
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Consider activities from 2019-06-28 to 2019-07-27.
-- 2. Group records by activity_date.
-- 3. Count distinct users active on each day.
-- 4. Return the date and active user count.

SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;