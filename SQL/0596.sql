-- Problem: Classes With at Least 5 Students
-- LeetCode ID: 596
-- Pattern: GROUP BY / HAVING
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Group records by class.
-- 2. Count the number of students in each class.
-- 3. Keep only classes having at least 5 students.

SELECT
    class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;