"""
기본 수학 2
- 소수 찾기 (1978)
- 소수 (2581)
- 소인수분해 (11653)
- 소수 구하기 (1929)
- 베르트랑 공준 (4948)
- 골드바흐의 추측 (9020)
"""
import sys
"""
<1978>
소수 찾기
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램
- Prime number(소수) : 1과 그수 자신 이외의 자연수로는 나눌 수 없는, 1보다 큰 자연수이다.

[input]
4
1 3 5 7

[output]
3
"""

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0

for num in numbers:
    no_prime = 0
    if num > 1: # 1보다 큰 경우
        for i in range(2, num):
            if num % i == 0: # 자기 자신 밑에 수와 나누어지는 경우
                no_prime += 1
            
        if no_prime == 0: # 나누어지는 수가 없는 경우
            count += 1
print(count)
                
"""
<2581>
소수
자연수 M과 N이 주어질 때  M 이상 N 이하 자연 수 중,
소수 인것을 모두 골라 합과 최솟값을 찾는 프로그램을 작성하시오. 

[input]
60
100

[output]
620
61
"""

# M과 N이 주어진다.
m = int(input())
n = int(input())
lst = list(range(m, n+1))

# M =< num <= N 자연수 중 소수인 것
lst1 = []

for num in lst:
    no_prime = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0 :
                no_prime +=1
                break  # 시간 초과 방지
        if no_prime == 0:
            lst1.append(num)

if len(lst1) == 0 :
    print(-1)
else :
    print(sum(lst1))
    print(min(lst1))

"""
<11653>
소인수분해
정수 N이 주어질떄, 소인수분해하는 프로그램 작성하기

[input]
72

[output]
2
2
2
3
3
"""

n = int(input())
m = 2
while n != 1: # 몫이 1이되면 멈춤.
    if n % m == 0: 
        n = n // m
        print(m)
    else : 
        m += 1 # 분해가 안되면 1 증가

"""
<1929> <= 여기부터
소수 구하기
M과 N 사이의 소수 구하기

[input]
3 16

[output]
3
5
7
11
13
"""

m,n = map(int, sys.stdin.readline().split())
arr = list()

for num in range(m,n+1):
    if num == 1:
        pass
    elif num == 2 or num == 3:
        arr.append(num)
    else :
        for j in range(2,num): # 2 ~ 5
            if num % j == 0: # 5 // 2 & 5 // 3 & 5 // 4
                break
            elif j == num-1: # 2 == 4 & 3 == 4 & 4 == 4
                arr.append(num) # 5

for num in arr:
    print(num)

# ------------------------------------------

def isPrime(num):
    if num == 1:
        return False
    else : 
        for i in range(2, int(num**0.5)+1): # 2부터 num의 제곱근 까지 검사하여 소수인지 판별
            if num % i == 0:
                return False
        return True

for i in range(m,n+1):
    if isPrime(i):
        print(i)

"""
<4948>
베르트랑 공준
n이 주어졌을 때 n보다 크고 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
- 베르트랑 공준 : 임의의 자연수 N에 대해 n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다.

[input]
1
10
13
100
1000
10000
100000
0

[output]
1
4
3
21
135
1033
8392
"""
n = 1
while True:
    lst = list()
    n = int(sys.stdin.readline())
    n2 = 2*n

    if n == 0:
        break
    elif n == 1:
        print(1)
        continue
    
    def isPrime(num):
        if num == 1:
            return False
        else : 
            for i in range(2, int(num**0.5)+1): 
                if num % i == 0:
                    return False
            return True

    for num in range(n+1, n2):    
        if isPrime(num):
            lst.append(num)         
    print(len(lst))

# --------------------------------

def isPrime(num):
    if num == 1: # 1은 모든 수의 약수 이므로 Pass
        return False
    else : 
        for i in range(2, int(num**0.5)+1):  # 제곱근이 있는 수 중에
            if num % i == 0: # 약수가 있으면 False
                return False
        return True # 이외에 수는 소수

while True:
    count = 0 # 갯수 조건
    n = int(input())
    if n == 0 : # 0을 입력하면 아웃
        break
    for i in range(n, 2*n+1): 
        if isPrime(i):
            count+= 1
    print(count)

# ----------------------------------

def isPrime(num):
    if num == 1: # 1은 모든 수의 약수 이므로 Pass
        return False
    else : 
        for i in range(2, int(num**0.5)+1):  # 제곱근이 있는 수 중에
            if num % i == 0: # 약수가 있으면 False
                return False
        return True # 이외에 수는 소수


all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if isPrime(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가

n = int(input())

while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음


"""
<9020>
골드바흐의 추측
2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

- 골드바흐의 수 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다. 
- 골드바흐의 파티션 : 짝수를 두 소수의 합으로 나타내는 표현 
- ex) 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7

[input]
3 (테스트 수)
8
10
16

[output]
3 5
5 5
5 11
"""

# 소수 집합 생성

nums = {x for x in range(2, 10_001) if x == 2 or x%2 == 1}
# 2와 홀수로 이루어진 집합

for odd in range(3, 101, 2): 
    nums -= {i for i in range(2* odd, 10_001, odd) if i in nums}
    # 홀수의 배수로 이루어진 집합은 제외

# 골드 바흐 수 출력
t = int(input())
for _ in range(t):
    even = int(input())
    half = even // 2 
    for x in range(half, 1, -1):  # 차이가 적은 두 수를 구하기 위해서 큰수부터 꺼냄
        if (even-x in nums) and (x in nums):  # even-x 와 x가 소수 집합에 포함 되었는지 확인
            print(x, even-x)  # 작은수부터 출력
            break
