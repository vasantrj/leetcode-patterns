/*
Problem: Customer Placing the Largest Number of Orders
LeetCode ID: 586
Pattern: SQL / GROUP BY / Aggregate Functions
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Group all orders by customer_number.
2. Count the number of orders placed by each customer.
3. Sort the counts in descending order.
4. Return the customer with the highest number of orders.
*/

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;