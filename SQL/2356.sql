-- Problem: Number of Unique Subjects Taught by Each Teacher
-- LeetCode ID: 2356
-- Pattern: GROUP BY / COUNT DISTINCT
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group records by teacher_id.
-- 2. Count distinct subjects taught by each teacher.
-- 3. Return teacher_id and the count.

SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;