"""
반복문
1. 빠른 A+B (15552)
2. 별 찍기 (2439)
3. A+B - 4 (10951)
4. 더하기 사이클 (1110)
"""

# 15552

import sys
t = int(input())

while t >= 1:
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    t -= 1

# 2439

stars = int(input())

for star in range(1, stars + 1): # range 5 => 0,1,2,3,4
    blank = stars - star
    print(" " * blank, "*" * star)

# 10951

while True:
    try:
       a,b = map(int, sys.stdin.readline().split()) 
       print(a+b)
    except:
        break

# 1110
'''
26 = 2 + 6 = 8 (1)
6 + 8 = 14 (2)
8 + 4 = 12 (3)
4 + 2 = 6 (4)
26

----
 1 => 1, 0 = 10  (앞에 0을 붙여 두 자리 수로 만들고)
 1 + 0 = 1 (각 자리의 숫자를 더한다.)
 0 + 1 = 1
 1 + 1 = 2
 1 + 2 = 3
 2 + 3 = 5

'''

len = 0
num = int(input())
head = num
new_num = None

while new_num != head:
    a = num // 10 # 십의 자리 수
    b = num % 10 # 일의 자리 수
    a_b = a+b # 십 + 일의 결과 값
    
    num = (b*10) + (a_b%10) 
    new_num = num
    len += 1

print(len)

