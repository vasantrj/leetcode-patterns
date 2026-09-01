-- Problem: Percentage of Users Attended a Contest
-- LeetCode ID: 1633
-- Pattern: GROUP BY / Aggregation
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Count total users from the Users table.
-- 2. Group registrations by contest_id.
-- 3. Compute:
--      (registered users / total users) * 100
-- 4. Round percentage to 2 decimal places.
-- 5. Sort by percentage descending, then contest_id ascending.

SELECT
    contest_id,
    ROUND(
        COUNT(user_id) * 100.0 /
        (SELECT COUNT(*) FROM Users),
        2
    ) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;