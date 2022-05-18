"""
기본 수학 2
- 소수 찾기 (1978)
- 소수 (2581)
- 소인수분해 (11653)
- 소수 구하기 (1929)
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

# n = int(input())
# numbers = list(map(int, sys.stdin.readline().split()))
# count = 0

# for num in numbers:
#     no_prime = 0
#     if num > 1: # 1보다 큰 경우
#         for i in range(2, num):
#             if num % i == 0: # 자기 자신 밑에 수와 나누어지는 경우
#                 no_prime += 1
            
#         if no_prime == 0: # 나누어지는 수가 없는 경우
#             count += 1
# print(count)
                
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

# # M과 N이 주어진다.
# m = int(input())
# n = int(input())
# lst = list(range(m, n+1))

# # M =< num <= N 자연수 중 소수인 것
# lst1 = []

# for num in lst:
#     no_prime = 0
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0 :
#                 no_prime +=1
#                 break  # 시간 초과 방지
#         if no_prime == 0:
#             lst1.append(num)

# if len(lst1) == 0 :
#     print(-1)
# else :
#     print(sum(lst1))
#     print(min(lst1))

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

# n = int(input())
# m = 2
# while n != 1: # 몫이 1이되면 멈춤.
#     if n % m == 0: 
#         n = n // m
#         print(m)
#     else : 
#         m += 1 # 분해가 안되면 1 증가

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

# for i in range(m,n+1):
#     no_prime = 0
#     if i > 1:
#         for x in range(2,i):
#             if i % x == 0:
#                 no_prime += 1
#                 break
#         if no_prime == 0:
#             print(i)


for num in range(m,n+1):
    for 
    if num == 2 or num == 3:
        print(num)
    elif num % 2 == 0 or num % 3 == 0:
        pass
    else :
        print(num)