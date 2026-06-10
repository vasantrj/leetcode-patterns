-- Problem: Not Boring Movies
-- LeetCode ID: 620
-- Pattern: Filtering / ORDER BY
-- Difficulty: Easy
--
-- Time Complexity: O(n log n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Select movies with odd-numbered ids.
-- 2. Exclude movies whose description is 'boring'.
-- 3. Sort the result by rating in descending order.

SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;