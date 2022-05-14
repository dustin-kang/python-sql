"""
937

로그를 재정렬한다.
"식별자 문자/숫자로그"

1. 각 로그(Each log)의 가장 앞 부분 식별자(identifier)이다.
2. 문자로그(letter-logs)가 숫자 로그 앞에 온다.
3. 문자(contents)가 동일한 경우 식별자 순으로 정렬한다.
4. 숫자 로그(digit-logs)는 입력 순서대로 한다.

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

letters, digits = [], []

for log in logs:
    if log.split()[1].isdigit(): # 2번에 의거해 슷자로그와 문자로그를 구분하여 저장한다.
        digits.append(log)
    else : 
        letters.append(log)

# 숫자로그는 입력 순서대로 그대로 저장한다.
# 문자로그는 문자로그 순서대로 하되 동일한 경우 식별자 순서대로 저장한다. (x.split()[0])
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print (letters + digits) # 리스트 이어 붙이기