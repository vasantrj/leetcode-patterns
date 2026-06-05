-- Problem: Big Countries
-- LeetCode ID: 595
-- Pattern: Filtering
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Select country name, population, and area.
-- 2. A country is considered "big" if:
--    - area >= 3,000,000
--      OR
--    - population >= 25,000,000
-- 3. Return all matching countries.

SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;