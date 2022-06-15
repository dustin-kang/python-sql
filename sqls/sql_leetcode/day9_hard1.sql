-- 185. Department Top Three Salaries
-- 부서별로 가장 많이 번 사람 순위


-- 601. Human Traffic of Stadium
-- 적어도 id가 3번 연속 100이상인 people 출력

-- 서브 쿼리 WITH 문
WITH T AS ( 
    SELECT T1.id, T1.visit_date, T1.people,
    T1.id - row_number() OVER(ORDER BY id) as grp
    FROM Stadium AS T1
    WHERE T1.people >= 100
)
-- ROW_NUMBER()은 분석함수이다. 지정된 행의 순서로 고유번호를 할당한다.
-- 2(id) - 1(고유번호) = 1 , 3(id) - 2(고유번호) = 1,  5(id) - 3(고유번호) = 2
SELECT T.id, T.visit_date, T.people
FROM T
WHERE grp in (select grp from T GROUP BY grp HAVING count(*) >= 3 )
-- GRP 갯수가 3개 이상인 데이터들만 출력