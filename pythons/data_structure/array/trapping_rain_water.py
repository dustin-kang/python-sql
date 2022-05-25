"""
42

빗물 트래핑
난이도 (상)
---
높이를 입력받아 비가 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

--input--
[0,1,0,2,1,0,1,3,2,1,2,1]
       _
   _   __ _
 _ __ ______
--output--
6
"""

"""
1. 투 포인터를 최대로 이동하는 방법
52밀리초

>> 투포인터(Two Pointers) 기법
어떠한 배열을 두고 시작점과 끝점 또는 왼쪽과 오른쪽 포인터 두지점을 기준으로 범위를 좁혀가며 문제를 푸는 방법
- 2개의 포인터가 좌우로 자유롭게 움직이며 문제를 풀이한다.
- 슬라이딩 윈도우와 비슷한점이 있지만 다른 방법이다.


- 오른쪽이 더 큰 경우 왼쪽에서 한 칸 앞으로 (left += 1)
- 왼쪽이 더 큰 경우 오른쪽에서 한 칸 앞으로 (right -=1)
이런식으로 서로 만나게 되면 O(n)으로 끝나게 된다.
"""

height = [0,1,0,2,1,0,1,3,2,1,2,1] # 빗물 트랩의 길이

def trap1(height):
    if not height: # 길이가 없는 경우에는 0으로 리턴
        return 0

    # 변수 정리 #
    volume = 0
    left, right = 0, len(height)-1 # 각 좌우의 초기 위치 (포인터)
    left_max, right_max = height[left], height[right] # 각 좌우의 최대 높이

    # 투 포인터 기법으로 가운데로 올때 까지 반복
    while left < right: # 왼쪽 인덱스가 오른쪽 인덱스만큼 올때까지 (다 조회하는 경우 종료)
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 최대높이 : 포인터가 변경될 때마다 값이 변경됨, max 값보다 작으면 그대로

        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max : # 오른쪽 높이가 더 큰 경우
            volume += left_max - height[left] # 기존 max 값에서 높이가 감소하면 감소한만큼 빗물 추가
            left += 1
        else : # 왼쪽 높이가 더 큰 경우
            volume += right_max - height[right]
            right -= 1

    return volume

# left :  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# right : 11 -> 10 -> 9 -> 8
# left_max : 0 -> 1 -> 2 -> 3
# right_max : 1 -> 1 -> 2
# volume : 0 -> 0 -> 0 -> 1 -> 1 -> 2 -> 4 -> 5 -> 6  

"""
2. 스택을 쌓는 방법
56밀리초
"""
def trap2(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우 #
        while stack and height[i] > height[stack[-1]]:
            
            top = stack.pop() # 스택을 꺼낸다.
            
            if not len(stack):
                break

            # 이전 차이 만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        # 변곡점이 없는 경우 인덱스 추가 #
        stack.append(i) 
    return volume

# print(trap1(height))  
print(trap2(height))  