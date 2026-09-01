-- Problem: Friend Requests II: Who Has the Most Friends
-- LeetCode ID: 602
-- Pattern: UNION ALL / GROUP BY
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(n)
--
-- Approach:
-- 1. Treat requester and accepter as friends by
--    combining both columns using UNION ALL.
-- 2. Count the number of occurrences of each user.
-- 3. Return the user with the highest friend count.

SELECT
    id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
) AS friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;
