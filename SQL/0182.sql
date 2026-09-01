-- Problem: Duplicate Emails
-- LeetCode ID: 182
-- Pattern: GROUP BY / HAVING
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group records by email.
-- 2. Count the occurrences of each email.
-- 3. Keep only emails that appear more than once.

SELECT email AS Email FROM Person
GROUP BY email HAVING COUNT(*) > 1;

