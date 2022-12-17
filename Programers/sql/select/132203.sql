-- 출처:https://school.programmers.co.kr/learn/courses/30/lessons/132203

SELECT DR_NAME, DR_ID, MCDP_CD, LEFT(HIRE_YMD,10) 
from doctor
where 
mcdp_cd = 'CS' or 
mcdp_cd = 'GS'
order by hire_ymd desc, dr_name asc