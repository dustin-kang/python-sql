-- 1873. Caculate Special Bonus
-- id가 홀수, 노동자 이름이 m으로 시작하지 않음 -> 보너스 0
SELECT employee_id, IF(employee_id % 2 != 0 and 
                       SUBSTRING(name, 1, 1) != 'M', salary, 0) AS bonus 
from Employees

-- 627. Swap Salary
-- 성별 교환 (UPDATE) sex가 f 면 m으로 변경 그렇지 않으면 f로 변경
UPDATE Salary
SET sex = if(sex = 'f', 'm', 'f')

-- 196. Delete Duplicate Emails
-- 중복 이메일 지우기(DELETE)
DELETE tb1
FROM Person as tb1, Person as tb2
WHERE tb1.Email = tb2.Email AND tb1.Id > tb2.Id;

-- 1667. Fix names in a Table
-- 테이블에 이름 고치기 (소문자 -> 대문자) 
-- CONCAT으로 문자열 합치기
select user_id, CONCAT(UPPER(substring(name,1,1)), LOWER(substring(name,2))) as name
from Users
order by user_id

-- 1484. Group Sold Products By The Date
-- 판매된 제품 날짜별로 그룹화
select sell_date,
        count(distinct product) as num_sold, -- 중복을 제거하고 제품 카운트
        GROUP_CONCAT(DISTINCT product ORDER BY product) AS products -- Group_concat으로 제품들 합치기
FROM Activities
group by sell_date

-- 1527. Patients With a Condition
-- DIAB1으로 시작하는 질병이 있는 환자 데이터만 가져오기
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'