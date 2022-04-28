"""
문자열
1. 아스키 코드 (11654)
2. 알파벳 찾기 (10809)
"""
import sys

# 11654
## ord(문자) : 뮨자를 유니코드 정수로 반환한다.
## chr(정수) : 정수를 해당하는 유니코드 문자로 반환한다.
# print(ord(input()))

# 10809
s = list(map(str, sys.stdin.readline()))
s.pop()
a = ord(s[0]) - ord('a') # 초기 인덱스

for i in s:
    ord(i)