"""
819

가장 흔한 단어

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
- 대소문자 구분 X
- 구두점 무시

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
        banned = ["hit"]
Output: "ball"

"""

import re
import collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]',' ',paragraph)
    # - 정규표현식 : \w(모든 문자)가 아닌(^) 모든 것을 ' '로 치환(Substitude)한다.
    .lower().split()
        if word not in banned] # 금지어는 포함하지 않는다.

counts = collections.Counter(words) # 개수를 처리하는 Counter 모듈을 사용한다.
for word in words:
    counts[word] += 1

print(counts.most_common(1)[0][0])
# a.most_common(1) : 가장 흔한 값을 추출한다. 
# [0][0] : 그중 첫번째 인덱스의 첫번째인 키 값을 가져온다. ( [('ball', 2)])