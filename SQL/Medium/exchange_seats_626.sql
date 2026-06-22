-- Problem: Exchange Seats
-- LeetCode ID: 626
-- Pattern: CASE WHEN
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Swap adjacent student ids:
--      odd id  -> id + 1
--      even id -> id - 1
-- 2. If the last row has an odd id and no partner,
--    keep it unchanged.
-- 3. Order by the new id sequence.

SELECT
    CASE
        WHEN id % 2 = 1 AND id != (SELECT MAX(id) FROM Seat)
            THEN id + 1
        WHEN id % 2 = 0
            THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;