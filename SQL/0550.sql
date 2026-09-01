-- Problem: Game Play Analysis IV
-- LeetCode ID: 550
-- Pattern: GROUP BY / JOIN / Conditional Aggregation
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Find each player's first login date.
-- 2. Check whether the player logged in again exactly
--    one day after their first login.
-- 3. Count such players.
-- 4. Divide by the total number of players.
-- 5. Round the result to 2 decimal places.

SELECT
    ROUND(
        COUNT(DISTINCT a.player_id) /
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM Activity a
JOIN (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) f
ON a.player_id = f.player_id
AND a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);