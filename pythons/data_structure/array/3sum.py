"""
015

세수의 합
---
배열을 입력받아 합으로 0을 만들 수  있는 3개의 Element를 출력하라.


--input--
nums = [-1,0,1,2,-1,-4]
nums = []
nums = [0]
--output--
[[-1,-1,2],[-1,0,1]]
[]
[]
"""
nums = [-1,0,1,2,-1,-4]

"""
1. 브루트 포스 계산
- O(n^3)으로 타임아웃 발생
- i,j,k를 활용하여 세가지 포인터로 0이라는 합을 찾아내는 방법 (i+j+k = 0)
- 중복된 값은 continue 처리
"""

def threesum1(nums):
    result = []
    nums.sort() # [-4,-1,-1,0,1,2]

    for i in range(len(nums)-2): # 4 (0까지)
        if i > 0 and nums[i] == nums[i-1]: # -4
            continue
        for j in range(i+1, len(nums)-1): # 5 (1까지)
            if j > i+ 1 and nums[j] == nums[j - 1]: # -1 -> -1 -> 0
                continue
            for k in range(j+1, len(nums)): # 6 (2까지)
                if j > j+ 1 and nums[k] == nums[k - 1]: # -1 -> 0 -> 1
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i],nums[j],nums[k]))
    return result


"""
2. 투 포인터로 합 계산
- left : 현재 i의 다음 지점
- right : 마지막 지점
- 간격을 좁혀가며 sum을 계산
    - sum > 0 : 오른쪽에서 간격을 좁힘
    - sum < 0 : 왼쪽에서 간격을 좁힘
- sum=0 인경우 어느 한쪽만 이동하는 것은 불가능, 전체 다 이동해야 함.
"""

def threesum2(nums):
    result = []
    nums.sort() # [-4,-1,-1,0,1,2]

    for i in range(len(nums)-2): # 4 (0까지)
        if i > 0 and nums[i] == nums[i-1]: # -4
            continue
        left, right = i + 1, len(nums) - 1 
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0: # 합계가 0보다 작은 경우
                left += 1
            elif sum > 0: # 합계가 0보다 큰 경우
                right -= 1
            else :
                # 정답인 경우 skip
                result.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left +1]:
                    left += 1
                while left < right and nums[right] == nums[right -1]:
                    left -= 1
                left += 1
                right -= 1
    return result

# +=         +=1   +=1   +=1    l>r    l,r+=1    l,r+=1   l>r
# left :  -1    -1     0     1      -1         0        1      1
# right :  2     2     2     2       2         1        0      0
# i :     -4    -4    -4    -4      -1        -1        1      2
# sum :   -3    -3    -2    -1       0         0        2      3
print(threesum2(nums))


"""
3. 2번 간소화 
"""
def threesum3(nums):
    result = []
    nums.sort()

    for i in range(len(nums)-1):
        if i != 0 and nums[i-1] == nums[i]:
            continue
        left, right = i+1, len(nums) -1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0: # 합계가 0보다 큰경우 우측에서 범위를 줄인다.
                right -= 1
            elif sum < 0 : # 합계가 0보다 작은 경우 좌측에서 범위를 줄인다.
                left += 1
            else :  # sum = 0 인경우 
                result.append([nums[i], nums[left], nums[right]])
                left += 1 # next
                while nums[left] == nums[left - 1] and left < right: # 만약에 다음 수가 이전 수랑 같은 경우
                    left +=1 # next 2번
    return result

