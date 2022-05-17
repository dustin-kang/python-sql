-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- 그룹핑 후  조건 처리
SELECT customer_id, count(customer_id) as count_no_trans
FROM Visits as v LEFT OUTER JOIN Transactions as t ON v.visit_id = t.visit_id
WHERE t.transaction_id is Null
GROUP BY v.customer_id
ORDER BY count_no_trans DESC

-- 1148. Article Views I
SELECT viewer_id as id
FROM Views
WHERE author_id = viewer_id
GROUP BY author_id
ORDER BY viewer_id ASC

-- 197. Rising Temperature
-- 이전 날씨보다 더우면 데이터를 가져온다. (DATEDIFF 아니면 SUBDATE 사용)
SELECT Weather.id
FROM Weather JOIN Weather as w ON DATEDIFF(weather.recordDate, w.recordDate) = 1  -- 현재날씨(weather) - 이전 날씨(w)의 차이(DATEDIFF)가 1인 데이터 조인
WHERE  Weather.Temperature > w.Temperature 

-- 607. Sales Person
-- 서브쿼리
SELECT
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN (SELECT
            o.sales_id
        FROM
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED')
;

-- 1890. The Latest Login in 2020
-- 날짜 관련 함수 YEAR() MAX()
SELECT user_id, max(time_stamp) as last_stamp
FROM Logins
WHERE YEAR(time_stamp) = '2020'
GROUP BY user_id


