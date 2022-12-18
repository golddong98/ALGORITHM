-- 출처:https://school.programmers.co.kr/learn/courses/30/lessons/131118

SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS , ROUND(AVG(b.review_score), 2) AS SCORE
FROM rest_info as a 
JOIN rest_review as b
ON a.REST_ID = b.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY a.rest_id
ORDER BY score DESC, FAVORITES DESC