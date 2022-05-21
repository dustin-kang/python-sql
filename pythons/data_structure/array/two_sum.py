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

nums = [3,2,4]
target = 6
lst = list()

for i in range(len(nums)): 
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            lst.append(i)
            lst.append(j)

print(lst)
