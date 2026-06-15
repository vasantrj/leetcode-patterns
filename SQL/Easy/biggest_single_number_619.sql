-- Problem: Biggest Single Number
-- LeetCode ID: 619
-- Pattern: GROUP BY / HAVING
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group numbers by value.
-- 2. Keep only numbers that appear exactly once.
-- 3. Return the maximum among those numbers.
-- 4. If no such number exists, MAX() returns NULL.

SELECT
    MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);