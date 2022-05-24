-- 1393.Capital Gain/Loss
-- Operation이 Buy인 데이터와 Sell인 데이터의 차이 -> Buy의 가격을 '-'하여 구한다.
SELECT stock_name, SUM(IF(operation='Buy',-price,price)) as capital_gain_loss 
FROM stocks
WHERE price
GROUP BY stock_name

-- 1407. Top Travellers
-- IFNULL(대상, 0) : null값이 존재하는 특성을 널값만 0으로 변경
SELECT u.name, IFNULL(SUM(distance),0) as travelled_distance
FROM Rides as r RIGHT JOIN Users as u ON r.user_id = u.id
GROUP BY r.user_id
ORDER BY travelled_distance DESC, name

-- 182. Duplicate Emails
-- 중복된 값 찾기 HAVING 을 이용하여 찾을 수 있다. (그룹화된 값들의 수를 찾음)
SELECT email
FROM Person
GROUP BY email
HAVING count(email) > 1

-- 1050. Actors and Directors Who Cooperated At Least Three Times
-- 배우와 감독 조합이 적어도 3번인 경우

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING count(actor_id) > 2 and count(director_id) > 2

-- 1587. Bank Account Summary II
SELECT u.name, SUM(amount) as balance
FROM Users as u JOIN Transactions as t ON u.account = t.account
GROUP BY t.account
HAVING balance > 10000

-- 1084. Sales Analysis III
-- 서브 쿼리를 사용하여 1월 1일 ~ 3월 3일(1분기)이 아닌(NOT IN) 날짜를 찾는다.
select distinct s.product_id, product_name
from Sales s join Product p on s.product_id = p.product_id
where s.product_id not in (select product_id  from Sales  where datediff(sale_date, '2019-01-01') < 0 or datediff(sale_date, '2019-03-31') > 0)

-- 1158. Market Analysis I << 여기서 부터 시작