"""
1차원 배열 & 함수
1. 최소 최대 (10818)
2. 최댓값 (2562)
3. 평균은 넘겠지 (4344)
4. 셀프 넘버 (4673)
5. 한수 (1065)
"""
import sys

# 10818

n = int(input()) # n개의 정수가 주어짐.
lst = list(map(int, sys.stdin.readline().split()))

a = min(lst)
b = max(lst)

print(f"{a} {b}")

# 10818 -2
cnt = int(input())
num = input().split(' ')
lst = []
for i in num:
    lst.append(int(i)) # num의 i요소를 리스트에 추가
    if len(lst) == cnt: # 리스트 길이랑 카운트 비교
       print(min(lst), max(lst))

# 2562

lst = []
while True :
    try:
        n = int(input())
        lst.append(n)
    except:
        print(max(lst))
        print(lst.index(max(lst))+1)
        break

# 4344

