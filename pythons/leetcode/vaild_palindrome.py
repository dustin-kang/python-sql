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
    if char.isalnum():
        lst.append(char.lower())
    else :
        pass

while len(lst) > 1 :
    if lst.pop(0) != lst.pop():
        print(False)
print(True)