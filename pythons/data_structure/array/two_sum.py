"""
001

두 수의 합
---
덧셈하여 target 을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.


--input--
nums = [2,7,11,15], target = 9
nums = [3,2,4], target = 6
nums = [3,3], target = 6

--output--
[0,1]
[1,2]
[0,1]
"""
"""
1. 브루트 포스로 계산한 방법
- 시간 복잡도 : O(n^2)
"""
nums = [3,2,4]
target = 6
lst = list()

for i in range(len(nums)):  # ex) 2 7 11 15 순으로 반복문 진행
    for j in range(i+1, len(nums)): # ex) 7 11 15 순으로 반복문 진행
        if nums[i] + nums[j] == target: # 만약 두 값의 합이 타겟값과 일치하는 경우
            lst.append(i) # 리스트의 추가
            lst.append(j)

print(lst)

"""
2. in을 이용한 탐색법
- 시간 복잡도 : O(n)
"""
for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i + 1:]:
        lst.append(nums.index(n))
        lst.append(nums[i + 1:].index(complement) + (i+1))

print(lst)

"""
3. 첫번째 수를 뺀 결과 키 조회
- 시간 복잡도 : O(1) ~ O(n)
- 딕셔너리를 사용하여 조회하기 때문에 시간 복잡도도 단축할 수 있다.
"""
nums_map = {}

for i, num in enumerate(nums):
    nums_map[num] = i # 키와 값의 위치를 바꿔 딕셔너리에 저장한다.

for i, num in enumerate(nums):
    if target - num in nums_map and i != nums_map[target - num]:
        # 두번째 수를 키로 조회하여 정답을 찾아낼 수 있다. 
        lst.append(nums.index(num))
        lst.append(nums_map[target - num])
        break
print(lst)

"""
4. 조회 구조 개선
- 시간 복잡도 : O(1) ~ O(n) (3번보다 더 간결함)
- 딕셔너리를 사용하여 조회하기 때문에 시간 복잡도도 단축할 수 있다.
"""
nums_map = {}

for i, num in enumerate(nums):
    if target - num in nums_map:
        lst.append(nums_map[target - num])
        lst.append(i)
    nums_map[num] = i # 딕셔너리에 존재하지 않으면 nums_map에 추가

print(lst)

