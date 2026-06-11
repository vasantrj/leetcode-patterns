-- Problem: Queries Quality and Percentage
-- LeetCode ID: 1211
-- Pattern: GROUP BY / Aggregation
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group records by query_name.
-- 2. Compute quality:
--      AVG(rating / position)
-- 3. Compute poor query percentage:
--      (count of rating < 3 / total queries) * 100
-- 4. Round both values to 2 decimal places.

SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(
        AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100,
        2
    ) AS poor_query_percentage
FROM Queries
GROUP BY query_name;