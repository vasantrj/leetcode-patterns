/*
Problem: Top Travellers
LeetCode ID: 1407
Pattern: SQL / LEFT JOIN / GROUP BY / Aggregate Functions
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Perform a LEFT JOIN so every user appears, even if they have no rides.
2. Sum the distance travelled by each user.
3. Replace NULL with 0 using IFNULL().
4. Group by user id and name.
5. Sort by travelled distance in descending order and name in ascending order.
*/

SELECT u.name, IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id,u.name
ORDER BY travelled_distance DESC, u.name ASC;