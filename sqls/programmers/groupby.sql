-- ANIMAL TYPE에 따른 동물 수
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) "count"
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE -- ANIMAL_TYPE에 따라서 데이터를 통계냄.
ORDER BY ANIMAL_TYPE

-- 동명 동물 수 찾기 (HAVING COUNT)
SELECT NAME, COUNT(NAME) "COUNT"
FROM ANIMAL_INS
GROUP BY NAME  HAVING COUNT >= 2 -- 동물의 이름이 두번 이상 쓰인 데이터 찾기  (= HAVING COUNT > 1)
ORDER BY NAME ASC

-- 9시부터 19:59분까지 각 시간대 별 입양 건수 찾기
SELECT HOUR(DATETIME) "HOUR", COUNT(*) "COUNT" -- DATETIME 을 통해 시간대 컬럼을 만든다.
FROM ANIMAL_OUTS
WHERE HOUR BETWEEN 9 AND 19 -- 해당 시간대를 조회한다.
GROUP BY HOUR -- HOUR 컬럼으로 묶는다. 
ORDER BY HOUR

-- 보호소에서 몇시에 입양이 가장 활발한지. 시간대(HOUR)별 입양건수 조사
SET @HOUR = -1;
SELECT (@HOUR := @HOUR +1) AS HOUR,
    (SELECT COUNT(HOUR(DATETIME)) 
        FROM ANIMAL_OUTS 
        WHERE HOUR(DATETIME)=@HOUR) AS COUNT  -- 변수와 같은 시간 컬럼으로 카운트 열을 생성한다. 
    FROM ANIMAL_OUTS
WHERE @HOUR < 23;