-- Problem: Product Price at a Given Date
-- LeetCode ID: 1164
-- Pattern: GROUP BY / LEFT JOIN
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Find the latest price change for each product
--    on or before '2019-08-16'.
-- 2. Join with Products to get the corresponding price.
-- 3. Products with no price change before that date
--    have the default price of 10.
-- 4. Return all product ids with their price on
--    '2019-08-16'.

SELECT
    p.product_id,
    IFNULL(pr.new_price, 10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM Products
) p
LEFT JOIN (
    SELECT
        product_id,
        new_price
    FROM Products
    WHERE (product_id, change_date) IN (
        SELECT
            product_id,
            MAX(change_date)
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
) pr
ON p.product_id = pr.product_id;