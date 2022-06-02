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