"""
238

자신을 제외한 배열의 곱
---
자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
나눗셈을 하지 않고 O(n)을 풀이하라


--input--
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
--output--
[24,12,8,6]
[0,0,9,0,0]
"""
"""
1. 큐(Queue)를 활용하여 곱셉
- 2개의 답을 통과했으나 다른 답이 시간 초과
"""
nums = [1,2,3,4]
temp = list()
answer = 1
lst = list()

# for i in range(0,len(nums)):
#     temp.append(nums.pop(0)) # 가장 첫번째 수를 제외
#     for a in nums: # 나머지 요소 곱셈
#         answer*=a
#     lst.append(answer) # 리스트에 추가
#     answer = 1 # 다시 1로 변경
#     nums.append(temp.pop()) # 제외된 수 뒤로 추가

# print(lst)

"""
2. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
- 시간 복잡도 : O(n)
"""

# 자신을 제외한 왼쪽 곱셈 결과와 오른쪽 곱셈 결과를 곱한다.

# 1. 왼쪽부터 곱하기
out = []
p = 1
for i in range(len(nums)):
    out.append(p) # [1,1,2,6]
    p = p * nums[i] # 1*1 -> 1*2 -> 2*3 -> 6*4

# 2. 오른쪽부터 곱하기
p = 1
for i in range(len(nums)-1, 0 -1, -1): # -1씩 감소 // 3 -> 2 -> 1 -> 0
    out[i] = out[i] * p # [3]=6, [2]=8, [1] = 12, [0]=24 
    p = p * nums[i] # 1, 4, 12, 24
print(out)