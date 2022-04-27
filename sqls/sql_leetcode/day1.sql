-- 584. Find Customer Referee
SELECT NAME
FROM Customer
WHERE COALESCE(referee_id, 0) != 2; --  Null 값이 아닌 첫 표현식을 리턴하는 함수, referee_id에 Null 값을 0으로 리턴

-- 175. Combine Two Tables
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person as p LEFT JOIN Address as a ON p.personId = a.personId

-- 176. Second Highest Salary (두번째로 큰 봉급)
SELECT max(Salary) "SecondHighestSalary"
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)

-- 178. Rank Scores
SELECT score, DENSE_RANK() OVER (ORDER BY Score DESC) AS 'Rank'
FROM Scores
---- 'OVER' : 괄호 안에 행의 범위 집합을 기준으로 작성하여 ORDER BY 와 PARTITION BY를 사용할 수 있다. 
---- DENSE_RANK() : 매출, 영업, 성적 등 순위를 표현할 때 사용합니다. RANK() 와 다르게 공백 없이 표현. ex) DR : 1-2-2-3-4 R: 1-2-2-4-5
