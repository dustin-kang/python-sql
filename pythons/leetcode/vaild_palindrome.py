"""
125
주어진 문자열이 팰린드롬인지 확인하는 문제
- 대소문자 구분 X
- 영문자 및 숫자만 해당
? 팰린드롬(회문) : 앞뒤가 똑같은 단어 또는 문장을 말함.

"A man, a plan, a canal : Panama" -> True
"race a car" -> False

"""

s = "A man, a plan, a canal: Panama"

lst = []

for char in s:
    if char.isalnum(): # 만약 알파벳 숫자라면
        lst.append(char.lower()) # 소문자로 리스트에 넣는다
    else :
        pass

while len(lst) > 1 : # 리스트 갯수가 1개일 때 까지 반복
    if lst.pop(0) != lst.pop(): # 맨 첫 자리와 맨 뒷자리 비교
        print(False) # 같지 않을 경우 False 출력
print(True)

# ---------------가장 빠른 방법----------------------

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s) # 정규표현식을 이용하는 방법
         
        return s == s[::-1] # 문자열 뒤집기


"""
- 반복문 보다 슬라이싱이 더 좋은 성능을 낸다.

>> 반복문에 strs를 데크 자료형으로 사용하면 좋은 성능으로 문제를 해결 할 수 있음
    - `strs : Deque = collections.deque()

>> s[::1] 로 문자열을 완전히 뒤집게 되면 속도를 더 낼 수 있다.
"""