"""
문자열
1. 아스키 코드 (11654)
2. 알파벳 찾기 (10809)
3. 문자열 반복 (2675)
4. 단어 공부 (1157)
5. 단어의 갯수 (1152)
6. 상수 (2908)
7. 다이얼 (5622)
"""
import sys

# 11654
## ord(문자) : 문자를 유니코드 정수로 반환한다.
## chr(정수) : 정수를 해당하는 유니코드 문자로 반환한다.
# print(ord(input()))

# # 10809
# word = input() 
# abc = list(range(97,123)) # 아스키코드의 숫자 범위

# for x in abc :
#     print(word.find(chr(x)))

# ## find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력하지만 index함수는 >AttributeError가 발생한다.

# # 2675
# t = int(input())
# while t != 0:
#         answer = "" # 출력문 변수 지정
#         r,s = map(str, input().split()) # 케이스 반복횟수와 문자열 s 지정
#         for i in s: # 문자요소 마다 반복
#             answer += f"{i* int(r)}"
#         print(answer) # 출력문 출력
#         t -= 1 # 테스트 케이스 갯수 감소 

# # 1157

# word = input().lower()
# word_list = list(set(word)) # set을 통해 중복을 제거 [p,s,i,m]
# cnt = []

# for i in word_list:
#     count = word.count(i) # 단어에서 알파벳 갯수 카운팅
#     cnt.append(count) # [1,4,4,1]

# if cnt.count(max(cnt)) >=2 :
#     print("2")
# else :
#     print(word_list[(cnt.index(max(cnt)))].upper())

# #1152
# word = input().split()
# print(len(word))

# # 2908
# a,b = map(int, input().split())
# a = int(f"{(a % 100) % 10}{(a % 100) // 10}{a // 100}")
# b = int(f"{(b % 100) % 10}{(b % 100) // 10}{b // 100}")

# if a > b :
#     print(a)
# else :
#     print(b)

