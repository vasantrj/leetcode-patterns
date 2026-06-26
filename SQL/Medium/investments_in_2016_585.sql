-- Problem: Investments in 2016
-- LeetCode ID: 585
-- Pattern: GROUP BY / Subquery
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(n)
--
-- Approach:
-- 1. Keep records whose tiv_2015 value appears more than once.
-- 2. Exclude records that share the same (lat, lon) location.
-- 3. Sum tiv_2016 for the remaining records.
-- 4. Round the final answer to 2 decimal places.

SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT
        lat,
        lon
    FROM Insurance
    GROUP BY
        lat,
        lon
    HAVING COUNT(*) = 1
);