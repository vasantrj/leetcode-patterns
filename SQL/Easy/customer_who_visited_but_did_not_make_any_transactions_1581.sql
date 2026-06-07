-- Problem: Customer Who Visited but Did Not Make Any Transactions
-- LeetCode ID: 1581
-- Pattern: LEFT JOIN / GROUP BY
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Left join Visits with Transactions using visit_id.
-- 2. Keep only visits with no matching transaction.
-- 3. Group by customer_id.
-- 4. Count the number of visits without transactions.

SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;