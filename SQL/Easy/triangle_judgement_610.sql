-- Problem: Triangle Judgement
-- LeetCode ID: 610
-- Pattern: CASE WHEN
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. A valid triangle must satisfy:
--      x + y > z
--      x + z > y
--      y + z > x
-- 2. Use CASE WHEN to check the triangle inequality.
-- 3. Return 'Yes' for valid triangles, otherwise 'No'.

SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z
         AND x + z > y
         AND y + z > x
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;