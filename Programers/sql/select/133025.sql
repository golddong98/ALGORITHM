-- 출처: https://school.programmers.co.kr/learn/courses/30/lessons/133025



SELECT a.FLAVOR
FROM FIRST_HALF as a
JOIN ICECREAM_INFO as b 
ON a.FLAVOR = b.FLAVOR
WHERE TOTAL_ORDER > 3000 and b.INGREDIENT_TYPE = "fruit_based"
ORDER BY TOTAL_ORDER DESC