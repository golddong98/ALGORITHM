-- 출처:https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT a.book_id,b.author_name ,LEFT(a.published_date,10) 
FROM BOOK as a 
JOIN AUTHOR as b 
ON a.author_id = b.author_id 
where CATEGORY = '경제' 
order by published_date ASC