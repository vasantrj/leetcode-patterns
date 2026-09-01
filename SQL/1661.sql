-- Problem: Average Time of Process per Machine
-- LeetCode ID: 1661
-- Pattern: SELF JOIN / GROUP BY
-- Difficulty: Easy
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Join Activity table with itself on:
--    - same machine_id
--    - same process_id
-- 2. Match start and end activities.
-- 3. Compute processing time:
--      end.timestamp - start.timestamp
-- 4. Average processing time for each machine.
-- 5. Round the result to 3 decimal places.

SELECT
    a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity a1
JOIN Activity a2
    ON a1.machine_id = a2.machine_id
   AND a1.process_id = a2.process_id
WHERE a1.activity_type = 'start'
  AND a2.activity_type = 'end'
GROUP BY a1.machine_id;