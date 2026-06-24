-- Problem: Restaurant Growth
-- LeetCode ID: 1321
-- Pattern: Window Function / Rolling Average
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(n)
--
-- Approach:
-- 1. Aggregate total revenue for each day.
-- 2. Use a 7-day rolling window to compute:
--      - Total revenue over the last 7 days.
--      - Average revenue over the last 7 days.
-- 3. Return results starting from the 7th day.
-- 4. Round the average amount to 2 decimal places.

WITH daily_sales AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT
    visited_on,
    SUM(amount) OVER (
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    ROUND(
        AVG(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS average_amount
FROM daily_sales
LIMIT 1000000 OFFSET 6;

