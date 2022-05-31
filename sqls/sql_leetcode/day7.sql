-- 1179. Reformat Department Table
-- 행열 변환
SELECT id,
SUM(CASE WHEN month='Jan' THEN revenue END) AS Jan_Revenue,
SUM(CASE WHEN month='Feb' THEN revenue END) AS Feb_Revenue,
SUM(CASE WHEN month='Mar' THEN revenue END) AS Mar_Revenue,
SUM(CASE WHEN month='Apr' THEN revenue END) AS Apr_Revenue,
SUM(CASE WHEN month='May' THEN revenue END) AS May_Revenue,
SUM(CASE WHEN month='Jun' THEN revenue END) AS Jun_Revenue,
SUM(CASE WHEN month='Jul' THEN revenue END) AS Jul_Revenue,
SUM(CASE WHEN month='Aug' THEN revenue END) AS Aug_Revenue,
SUM(CASE WHEN month='Sep' THEN revenue END) AS Sep_Revenue,
SUM(CASE WHEN month='Oct' THEN revenue END) AS Oct_Revenue,
SUM(CASE WHEN month='Nov' THEN revenue END) AS Nov_Revenue,
SUM(CASE WHEN month='Dec' THEN revenue END) AS Dec_Revenue    
FROM Department
GROUP BY id

-- 620. Not Boring Movies
SELECT *
FROM Cinema
WHERE (description != "boring") and (id%2 != 0)
ORDER BY rating desc

-- 596. Classes More Than 5 Students
SELECT class
FROM Courses
Group by class
HAVING count(class) >= 5

-- 181.  Employees Earning More Than Their Managers
-- 매니저보다 많이 버는 직원
SELECT e1.name AS Employee
FROM Employee as e1 JOIN Employee as e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary