"""
조건문
1. 두수 비교하기(1330)
2. 시험 성적 (9498)
3. 윤년 여부 (2753)
4. 알람 시계 (2884)
5. 오븐 시계 (2525)
6. 주사위 세개 (2480)
"""

# 1330
A, B = map(int, input().split())
if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')


# 9498
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else : print('F')

# 2753-1
# *윤년 : 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수 일 때.
year = int(input())
if (year % 4 == 0)& (year % 100 != 0):
    print(1)
elif year % 400 == 0:
    print(1)
else :
    print(0)

# 2753-2
year = int(input())
if ((year % 4 == 0)& (year % 100 != 0))\
    | (year % 400 == 0):
    print(1)
else :
    print(0)

# 2884
H, M = map(int, input().split())

def alram(H,M):
    if M < 45 :
        tmp = 45 - M
        M = 60 - tmp
        H -= 1
        if H == -1:
            H += 24
    else :
        M -= 45
    return print(f'{H} {M}')

alram(H,M)


# 2525
H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)

# 2480
# 주사위를 3개를 던져서
# 3개가 같으면 10000 + 같은눈 X 1000 의 상금
# 2개가 같으면 10000 + 같은눈 X 100 의 상금
# 모두 다른 눈이면 10000 + 그중 가장 큰 눈 X 100 의 상금

a,b,c = map(int, input().split())

if a == b == c :
    print(10000 + (a * 1000))
elif a == b or b == c :
    print(1000 + (b * 100))
elif a == c :
    print(1000 + (a * 100))
else :
    print(max(a,b,c) * 100)