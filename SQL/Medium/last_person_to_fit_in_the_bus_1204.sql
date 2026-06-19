-- Problem: Last Person to Fit in the Bus
-- LeetCode ID: 1204
-- Pattern: Window Function / Running Sum
-- Difficulty: Medium
--
-- Time Complexity: O(n log n)
-- Space Complexity: O(n)
--
-- Approach:
-- 1. Order passengers by turn.
-- 2. Compute the running total weight using SUM() OVER().
-- 3. Keep only rows where total weight <= 1000.
-- 4. The last such person is the answer.

SELECT person_name
FROM (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
) q
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;