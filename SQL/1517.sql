-- Problem: Find Users With Valid E-Mails
-- LeetCode ID: 1517
-- Pattern: Regular Expressions
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. A valid email must:
--      - Start with a letter.
--      - Contain only letters, digits, '_', '.', or '-'
--        before '@'.
--      - End with '@leetcode.com'.
-- 2. Use REGEXP to match the required pattern.
-- 3. Return all valid users.

SELECT user_id, name, mail
FROM Users
WHERE REGEXP_LIKE(mail, '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$', 'c');

