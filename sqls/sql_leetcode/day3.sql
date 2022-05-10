-- 1965. employees-with-missing-information
--UNION : 두가지 테이블을 합칠 수 있는 방법 == FULL OUTER JOIN
SELECT e.employee_id
FROM Employees as e, Salaries as s
WHERE e.employee_id not in (select employee_id from Salaries) -- 샐러리에 포함하지 않은 값
UNION
SELECT s.employee_id
FROM Employees as e, Salaries as s
WHERE s.employee_id not in (select employee_id from Employees)
ORDER BY employee_id


-- 1795.  Rearrange Products Table (store열 재배열)
-- price : store 열에 해당하는 가격
SELECT product_id, 'store1' as store, store1 as price 
FROM Products as p
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' as store, store2 as price
FROM Products as p
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' as store, store3 as price 
FROM Products as p
WHERE store3 IS NOT NULL

-- 608. Tree Node
SELECT id,
CASE
    WHEN p_id IS null then 'Root'
    WHEN id IN (select p_id from Tree) then 'Inner' --부모노드
    ELSE 'Leaf' -- 자식 노드
END as type
FROM Tree 