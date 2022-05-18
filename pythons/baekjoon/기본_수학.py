"""
기본 수학
1. 손익 분기점 (1712)
2. 벌집 (2292)
3. 분수 세기(1193)
4. 달팽이는 올라가고 싶다. (2869)
5. ACM 호텔 (10250)
6. 부녀 회장이 될테야 (2775)
7. 설탕 배달 (2839)
8. 큰 수 (10757)
"""
import sys

# 1712
"""
고정 비용(재산세, 임대료, 보험 급여등)  : A
가변 비용(재료, 인건) : B, 10개시 *10
노트북 가격 : C
손익분기점 : 총 수입 > 총 비용(고정 + 가변)
손익분기점이 존재하지 않은 경우 -1
"""
A,B,C = map(int, sys.stdin.readline().split())

if B >= C : # 가변 비용이 노트북 가격보다 같거나 클 경우 손익 분기점 존재 X
    print(-1)
else : 
    print(A//(C-B)+1)

# 2292
"""
숫자 N개가 주어졌을 경우, 1부터 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 작성하시오.
"""
n  = int(input())
num = 1 # 벌집의 갯수, 1부터 시작
cnt = 1
while n > num : # 수가 벌집 갯수보다 클 경우 (겹)
    num += 6 * cnt  # 6배로 증가
    cnt += 1
print(cnt)

# 1193 
"""
분수 찾기
- 사선에 따라 지그재그로 정수가 배열되고 분수가 매칭될때 정수 X가 주어지면 그에 대응하는 분수를 출력
1/1 
1/2 2/1 (+= a, -=b)
3/1 2/2 1/3 ( -= a, += b)
1/4 2/3 3/3 4/1 (+= a, -= b)
"""


n = int(input())
line = 0 # 라인 숫자
max_num = 0 # 해당 라인에서 가장 큰 숫자

while n > max_num: # 입력한 숫자가 해당 라인 가장 큰 숫자 안에 있으면 반복문 종료 
    line += 1
    max_num += line

gap = max_num - n
if line % 2 == 0 : # 짝수
    A = line - gap # 분자
    B = gap + 1 # 분모
else : # 홀수
    A = gap + 1 # 분자
    B = line - gap # 분모

print(f"{A}/{B}")

# 2869*
"""
달팽이가 V 미터인 막대에 낮에는 A만큼 올라가고 밤에는 B 만큼 미끄러진다.
정상에 올라가간 후에는 미끄러지지 않는다.
V 미터까지 몇일 걸리는가

[2(2) -> -1(1)] -> [2(3)-> -1(2)] -> [2(4) -> -1(3)] -> [2(5)] 4일

[5(5) -> -1(4)]
"""

a,b,v = map(int, sys.stdin.readline().split())

day = (v-b)/(a-b) # a * day -  b * (day - 1) > V
print(int(day) if day == int(day) else int(day)+1)


# 10250
"""
ACM 호텔
H : 층 수(Heigh)
W : 방 수(Width)
N : 번째 수 
가장 왼쪽 부터 높이가 낮은 순 우선
"""
num  = int(input())
for i in range(num):

    h,w,n = map(int, sys.stdin.readline().split())
    x = n // h + 1 # 호 수
    y = n % h # 층 수
    if n % h == 0: # 층 수 보다 작은 경우  
        x = n // h
        y = h
    print(f"{y*100+x}")

# 2775
"""
거주의 조건
자신의 아래(a-1)층의 1:b 호까지의 사람들의 수의 합 만큼 데려온다는 것을 지켜야한다.
k 층 n호에 몇명이 살고 있는지 출력해라

- 0층부터 있으며 0층 i호에는 i명이 산다는 전제.

입력 
Test case
k
n

3층 : 1호(1) 2호(1+4=5) 3호(1+4+10=15)
2층 : 1호(1) 2호(1+3=4) 3호(1+3+6=10) 4호(1+3+6+10=20)
1층 : 1호(1) 2호(1+2=3) 3호(1+2+3 =6) 4호(1+2+3+4=10)
-----------------------------------------------------
0층 : 1호(1) 2호(2) 3호(3) 4호(4)
"""
T = int(input())
s = 0
for _ in range(T):
    floor = int(input()) 
    num = int(input())
    f0 = [x for x in range(1, num+1)] # 0층 리스트
    for f in range(floor): # 층 만큼 먼저 반복
        for i in range(1, num): # 인덱스 조회를 통해 값 추가하기
            f0[i] += f0[i-1] # 사람 수 변경
    print(f0[-1]) # 가장 마지막 수 출력



# 2839
"""
설탕 배달
- 3kg 5kg
- 최대한 적은 봉지로 몇개를 가져가면 좋은가.
"""
n = int(input())

cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += (n // 5)
        print(cnt)
        break
    n -= 3
    cnt += 1
else :
    print(-1)


# 10757
"""
큰수  A+B

  9223372036854775807
+ 9223372036854775808
-----------------------
"""

a, b = map(str, sys.stdin.readline().split())
lst = []
tmp = 0
num = -1 # 일의 자리 수 부터 시작하기 때문에 인덱스 -1로 시작

while num != -len(a)-1: # 맨 처음 자리의 수까지 반복문
    some_num = int(a[num]) + int(b[num]) 

    if a[num] == a[0]: # 맨 처음 자리에 도달하면 break
        lst.insert(0, f'{some_num}')
        break
    if some_num // 10 == 0: # 자리 수의 합과 10의 나머지가 0인 경우 (10 미만)
        lst.insert(0,f'{some_num + tmp}')
        tmp = 0
    else : # 자리 수의 합과 10의 나머지가 0이 아닌 경우 (10 이상)
        lst.insert(0,f'{some_num % 10 + tmp}') # 이전 자리 수의 tmp를 더한다.
        tmp = some_num // 10
    num -= 1

print(int(''.join(lst)))