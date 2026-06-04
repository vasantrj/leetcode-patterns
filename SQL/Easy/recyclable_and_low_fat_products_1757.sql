-- Problem: Recyclable and Low Fat Products
-- LeetCode ID: 1757
-- Pattern: Filtering
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Select product_id from Products.
-- 2. Filter rows where:
--    - low_fats = 'Y'
--    - recyclable = 'Y'
-- 3. Return matching product IDs.

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';