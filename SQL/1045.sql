-- Problem: Customers Who Bought All Products
-- LeetCode ID: 1045
-- Pattern: GROUP BY / HAVING / COUNT DISTINCT
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group purchases by customer_id.
-- 2. Count distinct products bought by each customer.
-- 3. Compare with the total number of products.
-- 4. Keep customers who bought every product.

SELECT
    customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*)
    FROM Product
);