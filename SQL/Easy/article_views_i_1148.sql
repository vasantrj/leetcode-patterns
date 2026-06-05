-- Problem: Article Views I
-- LeetCode ID: 1148
-- Pattern: Filtering / DISTINCT
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Find rows where the author viewed their own article.
-- 2. author_id = viewer_id.
-- 3. Return distinct author IDs.
-- 4. Sort the result in ascending order.

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;