-- Problem: Customers Who Never Order
-- LeetCode ID: 183
-- Pattern: LEFT JOIN
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Perform a LEFT JOIN between Customers and Orders.
-- 2. Match customers using customerId.
-- 3. Customers with no matching order will have NULL
--    in the Orders table.
-- 4. Return the names of those customers.

SELECT c.name AS Customers
FROM Customers c LEFT JOIN Orders o ON c.id = o.customerId WHERE o.customerId IS NULL;
