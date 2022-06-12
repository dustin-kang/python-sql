"""
[739]
일일 온도
- 문제 : 매일의 화씨온도(F) 리스트를 입력받아, 더 따뜻한 날씨를 위해 며칠을 더 기다려야 하는지 출력해라


- 난이도 : ⭐️⭐️
- 시간복잡도 : O(1)


[EXAMPLE 1]
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

[EXAMPLE 2]
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

[EXAMPLE 3]
Input: temperatures = [30,60,90]
Output: [1,1,0]

"""


temperatures_1 = [73,74,75,71,69,72,76,73]
temperatures_2 = [30,40,50,60]
temperatures_3 = [30,60,90]

def daily_temperatures(T : list):
    """
    ### 스택 값을 비교하여 처리하는 방법
    
    1. 5번째 인덱스의 온도(72도)가 스택이 [2,3,4]이다.
        - 낮았던 이전 온도의 인덱스가 `[2,3,4]` 이다.
    2. 스택의 갯수가 0이 아니고, 현재온도 > 이전온도 인 경우
    3. 현 온도 인덱스와 이전 온도 인덱스의 차이를 `answer`에 넣는다.

    """
    answer = [0] * len(T) # 온도 요소의 개수 만큼 리스트 비워 놓기
    stack = [] # 현재 온도 인덱스와 이전 온도 인덱스의 차이를 계산할 스택
    for i, current in enumerate(T):
        # 현재 온도가 스택 값보다 높은 경우 정답 처리
        while stack and current > T[stack[-1]]:
            # 스택이 안비었고, 현재 온도가 이전 온도(T[stack[-1]])보다 높은 경우
            last = stack.pop() # 스택에서 팝으로 제거 
            answer[last] = i - last 
        stack.append(i)

    return answer