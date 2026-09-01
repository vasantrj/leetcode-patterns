-- Problem: Fix Names in a Table
-- LeetCode ID: 1667
-- Pattern: String Functions
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Convert the first character of each name to uppercase.
-- 2. Convert the remaining characters to lowercase.
-- 3. Order the result by user_id.

SELECT user_id, CONCAT( UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name FROM Users ORDER BY user_id;
