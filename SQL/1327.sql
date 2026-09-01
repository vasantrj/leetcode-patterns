-- Problem: List the Products Ordered in a Period
-- LeetCode ID: 1327
-- Pattern: JOIN / GROUP BY
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Products and Orders using product_id.
-- 2. Consider only orders placed in February 2020.
-- 3. Group by product name.
-- 4. Sum the ordered units for each product.
-- 5. Return products whose total ordered units
--    are at least 100.

SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o
    ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;