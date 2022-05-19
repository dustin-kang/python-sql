-- 1141. User Activity for the Past 30 Days I
-- 해당 기간에 따라, 하루라도 사용한 사람 수  구하기
SELECT activity_date as day, COUNT(DISTINCT(user_id)) as active_users
FROM Activity
WHERE activity_date between date("2019-06-28") and date("2019-07-27") -- 한달 범위
-- DATEDIFF('2019-07-27', activity_date) < 30 AND activity_date <= '2019-07-27'
GROUP BY activity_date

-- 1693. Daily Leads and Partners
SELECT date_id, make_name, count(distinct(lead_id)) as unique_leads , count(distinct(partner_id)) as unique_partners
FROM DailySales
GROUP BY make_name, date_id

-- 1729. Find Followers Count
SELECT user_id, COUNT(DISTINCT(follower_id)) as followers_count
FROM Followers
GROUP BY user_id

-- 586. Customer Placing the Largest Number of Orders
SELECT customer_number
FROM Orders
GROUP BY customer_number
-- sort by largest to smallest
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 511. Game Play Analysis I
-- 처음 로그인한 날짜
SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id

-- 1741. Find Total Time Spent by Each Employee
-- 사용자의 날짜별 사용 시간
SELECT event_day as day, emp_id, SUM(out_time - in_time) as total_time
FROM Employees
GROUP BY emp_id, event_day