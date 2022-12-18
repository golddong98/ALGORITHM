-- 출처:https://school.programmers.co.kr/learn/courses/30/lessons/144853


SELECT book_id, LEFT(published_date, 10)
FROM BOOK
WHERE category='인문' AND published_date LIKE '2021%'
order by published_date ASC