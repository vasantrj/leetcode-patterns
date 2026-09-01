-- Problem: Employees Earning More Than Their Managers
-- LeetCode ID: 181
-- Pattern: Self JOIN
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Perform a self join on the Employee table.
-- 2. Match each employee with their manager using
--    employee.managerId = manager.id.
-- 3. Filter employees whose salary is greater than
--    their manager's salary.
-- 4. Return the employee names.

SELECT e.name AS Employee
FROM Employee e JOIN Employee m ON e.managerId = m.id WHERE e.salary > m.salary;
