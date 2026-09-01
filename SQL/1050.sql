/*
Problem: Actors and Directors Who Cooperated At Least Three Times
LeetCode ID: 1050
Pattern: SQL / GROUP BY / HAVING
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Group the records by actor_id and director_id.
2. Count how many times each actor-director pair appears.
3. Use HAVING to keep only pairs that cooperated at least 3 times.
*/

SELECT
    actor_id,
    director_id
FROM ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING COUNT(*) >= 3;