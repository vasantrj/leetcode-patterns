-- Problem: Delete Duplicate Emails
-- LeetCode ID: 196
-- Pattern: DELETE / SELF JOIN
-- Difficulty: Easy
--
-- Time Complexity: O(n²)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Self-join the Person table on email.
-- 2. Match rows having the same email.
-- 3. Delete the row with the larger id,
--    keeping the smallest id for each email.

DELETE p1 FROM Person p1
JOIN Person p2 ON p1.email = p2.email WHERE p1.id > p2.id;

