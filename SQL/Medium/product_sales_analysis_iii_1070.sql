-- Problem: Product Sales Analysis III
-- LeetCode ID: 1070
-- Pattern: GROUP BY / JOIN
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Find the first year each product was sold.
-- 2. Join back with Sales to get the corresponding
--    quantity and price for that year.
-- 3. Return product_id, first_year, quantity, and price.

SELECT
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) f
ON s.product_id = f.product_id
AND s.year = f.first_year;