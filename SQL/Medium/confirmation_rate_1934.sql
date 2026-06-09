-- Problem: Confirmation Rate
-- LeetCode ID: 1934
-- Pattern: LEFT JOIN / GROUP BY / Conditional Aggregation
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Start from Signups to include all users.
-- 2. LEFT JOIN with Confirmations on user_id.
-- 3. Count confirmed actions and total confirmation requests.
-- 4. Compute:
--      confirmed / total
-- 5. Users with no confirmations get a rate of 0.
-- 6. Round the result to 2 decimal places.

SELECT
    s.user_id,
    ROUND(
        IFNULL(
            AVG(c.action = 'confirmed'),
            0
        ),
        2
    ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id;