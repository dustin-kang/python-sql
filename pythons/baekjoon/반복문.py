"""
반복문
1. 빠른 A+B (15552)
2. 별 찍기 (2439)
3. A+B - 4 (10951)
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
