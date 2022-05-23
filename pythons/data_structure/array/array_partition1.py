"""
561

배열 파티션 1
---
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰수를 출력하라


--input--
nums = [1,4,3,2]
nums = [6,2,6,5,1,2]

--output--
4
9
"""
"""
1. 짝수 번째 값으로 계산
- 시간 복잡도 : O(n)
"""

nums = [1,4,3,2]

sum = 0
nums.sort() # 작은 순으로 정렬

for i , n in enumerate(nums):
    if i % 2 == 0:
        sum += n
print(sum)

"""
2. 파이썬 다운 방식
- 시간 복잡도 : O(n)
"""
print(sum(sorted(nums)[::2]))