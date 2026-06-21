-- Problem: Count Salary Categories
-- LeetCode ID: 1907
-- Pattern: CASE WHEN / Aggregation
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Categorize accounts into:
--      Low Salary    : income < 20000
--      Average Salary: 20000 <= income <= 50000
--      High Salary   : income > 50000
-- 2. Count accounts in each category.
-- 3. Return all three categories even if their count is 0.

SELECT 'Low Salary' AS category,
       COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000

UNION ALL

SELECT 'Average Salary' AS category,
       COUNT(*) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000

UNION ALL

SELECT 'High Salary' AS category,
       COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000;
