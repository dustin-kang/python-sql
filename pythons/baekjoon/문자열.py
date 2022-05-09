"""
문자열
1. 아스키 코드 (11654)
2. 알파벳 찾기 (10809)
3. 문자열 반복 (2675)
4. 단어 공부 (1157)
5. 단어의 갯수 (1152)
6. 상수 (2908)
7. 다이얼 (5622)
8. 크로아티아 알파벳 (2941)
9. 그룹 단어 체커 (1316)
"""
import sys

# 11654
# ord(문자) : 문자를 유니코드 정수로 반환한다.
# chr(정수) : 정수를 해당하는 유니코드 문자로 반환한다.
print(ord(input()))

# 10809
word = input() 
abc = list(range(97,123)) # 아스키코드의 숫자 범위

for x in abc :
    print(word.find(chr(x)))

## find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력하지만 index함수는 >AttributeError가 발생한다.

# 2675
t = int(input())
while t != 0:
        answer = "" # 출력문 변수 지정
        r,s = map(str, input().split()) # 케이스 반복횟수와 문자열 s 지정
        for i in s: # 문자요소 마다 반복
            answer += f"{i* int(r)}"
        print(answer) # 출력문 출력
        t -= 1 # 테스트 케이스 갯수 감소 

# 1157

word = input().lower()
word_list = list(set(word)) # set을 통해 중복을 제거 [p,s,i,m]
cnt = []

for i in word_list:
    count = word.count(i) # 단어에서 알파벳 갯수 카운팅
    cnt.append(count) # [1,4,4,1]

if cnt.count(max(cnt)) >=2 :
    print("2")
else :
    print(word_list[(cnt.index(max(cnt)))].upper())

#1152
word = input().split()
print(len(word))

# 2908
a,b = map(int, input().split())
a = int(f"{(a % 100) % 10}{(a % 100) // 10}{a // 100}")
b = int(f"{(b % 100) % 10}{(b % 100) // 10}{b // 100}")

if a > b :
    print(a)
else :
    print(b)

# 5622-1
dial = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9] # 알파벳에 상응하는 수
alpha = list(range(65,91)) # 알파벳
a = 0 # 정답
lst = list(map(str, sys.stdin.readline())) # 입력을 받는다.
lst.pop()

for i in lst:
        c = alpha.index(ord(i)) # 알파벳의 인덱스를 이용하여 다이얼 수를 구한다.
        a += dial[c]+1 # 초계산을 위해 1을 추가한다.

print(a)

# 5622-2
alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  # 중첩 반복문
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리 # ABC -> A, B, C
        for x in word :  # 입력받은 문자를 하나씩 분리 
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
print(time)

# 2941 *
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*') # 문자와 동일한 변수 사용
print(len(word))

# 1316
# 그룹단어 : 각 문자가 연속해서 나타나는 경우

num = int(input()) # 3
result = num # 3

for i in range(0,num):
    word = input() # happy new year
    for elem in range(0, len(word)-1): 
        if word[elem] == word[elem+1]: # 연속하는 경우
            pass
        elif word[elem] in word[elem+1:]: # 현 알파벳이 이후 단어로 나오는 경우 (연속 X)
            result -= 1  # 1 점 깎고
            break # 다음 단어로
print(result)

    
