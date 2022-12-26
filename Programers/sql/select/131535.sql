-- 출처:https://school.programmers.co.kr/learn/courses/30/lessons/131535


SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE LEFT(JOINED,4) = '2021' AND AGE >=20 AND AGE <= 29