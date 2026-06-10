-- Problem: Average Selling Price
-- LeetCode ID: 1251
-- Pattern: JOIN / Aggregation
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Prices and UnitsSold using product_id.
-- 2. Ensure purchase_date falls within the price validity period.
-- 3. Compute:
--      total revenue = SUM(price * units)
--      total units   = SUM(units)
-- 4. Average price = revenue / units.
-- 5. Products with no sales should return 0.
-- 6. Round the result to 2 decimal places.

SELECT
    p.product_id,
    ROUND(
        IFNULL(
            SUM(p.price * u.units) / SUM(u.units),
            0
        ),
        2
    ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
   AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;