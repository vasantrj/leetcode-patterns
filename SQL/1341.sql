-- Problem: Movie Rating
-- LeetCode ID: 1341
-- Pattern: JOIN / GROUP BY / UNION
-- Difficulty: Medium
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
--
-- Approach:
-- 1. Find the user who rated the greatest number of movies.
--    If there is a tie, choose the lexicographically smallest name.
-- 2. Find the movie with the highest average rating in February 2020.
--    If there is a tie, choose the lexicographically smallest title.
-- 3. Combine both results using UNION ALL.

(
    SELECT u.name AS results
    FROM MovieRating mr
    JOIN Users u
        ON mr.user_id = u.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name
    LIMIT 1
)

UNION ALL

(
    SELECT m.title AS results
    FROM MovieRating mr
    JOIN Movies m
        ON mr.movie_id = m.movie_id
    WHERE DATE_FORMAT(mr.created_at, '%Y-%m') = '2020-02'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title
    LIMIT 1
);