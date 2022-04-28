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
c = int(input())
while c != 0:
    lst = list(map(int, sys.stdin.readline().split()))
    a = lst.pop(0) # 그룹 내 인원 수
    m = sum(lst) / a # 반 평균
    t = 0 # 반 평균을 넘는 인원

    for num in lst:
        if num > m:
            t += 1
        else : pass
    
    print(f"{round(100*(t / a),3)}%")
    
    c -=1

# 4344-1
c = int(input())
def avg(c):
  while c != 0:
    score = list(map(int, input().split(" ")))
    n = score.pop(0) # 그룹 내 인원 수
    upper_n = 0 # 반 평균을 넘는 인원
    avg = sum(score) / n # 반 평균
    for i in range(0, n):
      if score[i] > avg: # 반 평균을 넘으면
          upper_n += 1 # 인원을 추가한다.
      else : 
        pass
    rate = (upper_n / n) * 100 # 확률 
    result = f'{rate:.3f}%'
    c -= 1
    print(result)

avg(c)

# 4673
# 33 => 33 + 3 + 3 = 39 ...
nums = list(range(1, 10_001)) # 10_001 = 10000
remove_list = []

for num in nums: # 리스트 안 숫자
  for n in str(num): # 숫자의 문자열 945 = '9''4''5'
    num += int(n) # 9 + 4 + 5
  if num  <= 10_000: # 만약 그 수가 만보다 작거나 같을 경우
    remove_list.append(num) # 넣는다. 

for remove_num in set(remove_list): # set을 통해 중복값을 제거한다.
  nums.remove(remove_num) # nums 중 생성자 수 제거

for self_num in nums: # self number 출력
  print(self_num)

# 1065
# 한수 : 양의 정수 X의 각 자리가 등차수열을 이루는 수
# 등차수열 : 숫자와 숫자 사이의 간격이 동일한 숫자의 나열

nums = int(input())
hansu = 0

for num in range(1, nums+1):
    num_lst = list(map(int, str(num))) # 숫자 num을 문자열로 변경해 각 자리수를 분리시킨 다음, int 타입으로 변환함.
    if num < 100: # 100보다 작으면 모두 한수이다.
        hansu += 1
    elif num_lst[0] - num_lst[1] == num_lst[1] - num_lst[2]:
        hansu += 1 # X의 각자리가 등차수열이면 한수 이다.

print(hansu)