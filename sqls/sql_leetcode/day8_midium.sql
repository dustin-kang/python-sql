--177. Nth Highest Salary
-- issues 참조
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN (
# Write your MySQL query statement below.
SELECT C.salary
FROM(
SELECT salary,
DENSE_RANK() OVER(ORDER BY salary DESC ) AS 'RANK'
FROM Employee
) as C
WHERE C.RANK = N
ORDER BY C.salary limit 1
);
END

--184. Department Highest Salary
SELECT
    D.name AS 'Department',
    E.name AS 'Employee',
    E.salary AS 'Salary'
FROM
    Employee AS E JOIN
    Department AS D ON
    E.departmentId = D.id
WHERE
    (E.DepartmentID, Salary) IN
    ( SELECT
            DepartmentId, MAX(Salary)
      FROM
            Employee
      GROUP BY DepartmentId
    )
;

--626. Exchange Seats
-- 짝수 학생과 홀수 학생의 데이터 교체
SELECT id,
CASE 
    WHEN id % 2 = 0 THEN (SELECT student FROM Seat where id = (s.id-1))
    -- 짝수인 경우 id - 1 인 학생으로
    WHEN id % 2 != 0 AND id < (SELECT COUNT(student) from Seat) THEN (SELECT student FROM seat WHERE id = (s.id+1))
    -- 홀수인 경우 와 총 학생수보다 작은 경우는 id + 1 인 학생으로
    ELSE student
    -- 그외(마지막)인 경우는 그대로
END AS student
FROM Seat AS s


SELECT
	CASE
		WHEN seat.id % 2 != 0 AND seat.id = (SELECT COUNT(*) FROM seat) THEN seat.id -- 마지막 학생
		WHEN seat.id % 2 = 0 THEN seat.id - 1 -- 짝수 학생
		ELSE
			seat.id + 1 -- 홀수 학생
	END as id,
	student 
FROM seat
ORDER BY id
;

SELECT
IF (id < (SELECT COUNT(*) FROM Seat), IF (id MOD 2 = 0, id-1, id+1), if(id MOD 2 = 0, id-1, id)) AS id, student
FROM Seat
ORDER BY id ASC;

-- MODE(200, 7) => 4 나머지를 구하는 연산