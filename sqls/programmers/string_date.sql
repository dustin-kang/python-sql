-- Lucy 가 포함된 이름의 데이터 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID ASC

-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE ('%el%') AND ANIMAL_TYPE = 'Dog' -- 이름에 el이 들어가는 강아지 찾기
ORDER BY NAME

-- 중성화 여부 파악하기 (풀이 1) : CASE WHEN IN 풀이
SELECT ANIMAL_ID, NAME, 
    (CASE 
        WHEN SEX_UPON_INTAKE IN ('Neutered Male', 'Spayed Female') THEN 'O'
        ELSE 'X' END '중성화')
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- 중성화 여부 파악하기 (풀이 2) : CASE WHEN LIKE 풀이
SELECT ANIMAL_ID, NAME, 
    CASE WHEN (SEX_UPON_INTAKE LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%')
    THEN 'O' ELSE 'X' END AS '중성화' 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID ASC

-- 중성화 여부 파악하기 (풀이 3) : IF 문 풀이
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%','O','X') AS '중성화'
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID ASC

-- 오랜 기간 보호한 동물 두마리 조회 작성 : ANIMAL_ID가 외래키

SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS AS INS
INNER JOIN ANIMAL_OUTS AS OUTS 
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY DATEDIFF(OUTS.DATETIME, INS.DATETIME) DESC -- DATEDIFF 두 날짜간 차이 
LIMIT 2;

-- DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') "날짜" -- 데이터 포맷 활용
FROM ANIMAL_INS
ORDER BY ANIMAL_ID