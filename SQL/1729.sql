-- Problem: Find Followers Count
-- LeetCode ID: 1729
-- Pattern: GROUP BY / COUNT
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group records by user_id.
-- 2. Count the number of followers for each user.
-- 3. Sort the result by user_id.

SELECT
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;