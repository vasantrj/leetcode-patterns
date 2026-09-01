-- Problem: Group Sold Products By The Date
-- LeetCode ID: 1484
-- Pattern: GROUP BY / String Aggregation
-- Difficulty: Easy
--
-- Time Complexity: O(n log n)
-- Space Complexity: O(n)
--
-- Approach:
-- 1. Group records by sell_date.
-- 2. Count the number of distinct products sold each day.
-- 3. Concatenate distinct product names in
--    alphabetical order using GROUP_CONCAT().
-- 4. Return the results ordered by sell_date.

SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(
        DISTINCT product
        ORDER BY product
        SEPARATOR ','
    ) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
