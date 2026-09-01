/*
Problem: Sales Person
LeetCode ID: 607
Pattern: SQL / Subquery / JOIN / NOT IN
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Find all sales_id values that have sold to the company named 'RED'.
2. Use a JOIN between Orders and Company to identify these salespersons.
3. Select salespersons whose sales_id is NOT IN that list.
4. Return their names.
*/

SELECT s.name
FROM SalesPerson s
WHERE s.sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);