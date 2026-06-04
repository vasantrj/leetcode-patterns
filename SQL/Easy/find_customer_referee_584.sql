-- Problem: Find Customer Referee
-- LeetCode ID: 584
-- Pattern: Filtering / NULL Handling
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Select customer names.
-- 2. Exclude customers whose referee_id = 2.
-- 3. Include customers with NULL referee_id
--    because they were not referred by anyone.
-- 4. Return the remaining names.

SELECT name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;