-- 출처: https://school.programmers.co.kr/learn/courses/30/lessons/132202

SELECT MCDP_CD AS 진료과코드, COUNT(APNT_YMD) AS 5월예약건수
FROM APPOINTMENT
WHERE MID(APNT_YMD,1,7) = '2022-05'
GROUP BY MCDP_CD
ORDER BY 5월예약건수 ASC, 진료과코드 ASC