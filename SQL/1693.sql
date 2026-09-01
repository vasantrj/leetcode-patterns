/*
Problem: Daily Leads and Partners
LeetCode ID: 1693
Pattern: SQL / GROUP BY / COUNT DISTINCT
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Group the records by date_id and make_name.
2. Count the distinct lead_id values for each group.
3. Count the distinct partner_id values for each group.
4. Return the grouped results.
*/

SELECT date_id,make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id,make_name;