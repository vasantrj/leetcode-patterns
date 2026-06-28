-- Problem: Patients With a Condition
-- LeetCode ID: 1527
-- Pattern: String Matching
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Select patients whose conditions contain the
--    diabetes code "DIAB1".
-- 2. Match either:
--      - At the beginning of the string, or
--      - Preceded by a space.
-- 3. Return all columns.

SELECT * FROM Patients WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
