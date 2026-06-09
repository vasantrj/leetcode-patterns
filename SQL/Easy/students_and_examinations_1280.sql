-- Problem: Students and Examinations
-- LeetCode ID: 1280
-- Pattern: CROSS JOIN / LEFT JOIN / GROUP BY
-- Difficulty: Easy
--
-- Time Complexity: O(S × U + E)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Generate all possible student-subject pairs using CROSS JOIN.
-- 2. LEFT JOIN with Examinations to include attendance records.
-- 3. Count how many times each student attended each subject exam.
-- 4. Group by student and subject.
-- 5. Order by student_id and subject_name.

SELECT
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
    ON s.student_id = e.student_id
   AND sub.subject_name = e.subject_name
GROUP BY
    s.student_id,
    s.student_name,
    sub.subject_name
ORDER BY
    s.student_id,
    sub.subject_name;