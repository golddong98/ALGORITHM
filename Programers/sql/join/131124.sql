-- 출처:https://school.programmers.co.kr/learn/courses/30/lessons/131124

SELECT t2.MEMBER_NAME, t1.REVIEW_TEXT, left(t1.review_date,10) AS REVIEW_DATE
FROM REST_REVIEW AS t1
JOIN MEMBER_PROFILE AS t2
ON t1.member_id = t2.member_id
WHERE t1.member_id = (
    SELECT member_id
    FROM rest_review
    GROUP BY member_id
    ORDER BY count(review_id) DESC
    LIMIT 1
)
Order BY review_date ,REVIEW_TEXT