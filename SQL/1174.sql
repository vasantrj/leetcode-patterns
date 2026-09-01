-- Problem: Immediate Food Delivery II
-- LeetCode ID: 1174
-- Pattern: GROUP BY / Conditional Aggregation
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Find each customer's first order date.
-- 2. Check whether the first order was delivered on the
--    customer's preferred delivery date.
-- 3. Count immediate first orders.
-- 4. Compute the percentage of immediate orders among all customers.
-- 5. Round the result to 2 decimal places.

SELECT
    ROUND(
        AVG(order_date = customer_pref_delivery_date) * 100,
        2
    ) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT
        customer_id,
        MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);