-- Problem: Monthly Transactions I
-- LeetCode ID: 1193
-- Pattern: GROUP BY / Conditional Aggregation
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group transactions by month and country.
-- 2. Count total transactions and approved transactions.
-- 3. Sum transaction amounts and approved amounts.
-- 4. Use conditional aggregation for approved metrics.

SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY
    DATE_FORMAT(trans_date, '%Y-%m'),
    country;