"""
브루트 포스
- 블랙잭 (2798)
- 분해합 (2231)
- 덩치 (7568)
- 체스판 다시 칠하기 (1018)
- 영화 감독 숌 (1436)
"""
import sys
"""
2798
블랙잭

카드의 합이 21이 넘지 않은 한도에서 카드의 합을 최대한 크게 만드는 게임
N장의 카드 중 3장을 골라야 한다.
카드의 합이 M과 최대한 가깝게 만든다.


[입력]
카드 갯수 N, M
카드에 쓰여진 수 N장 

[출력]
M을 넘지 않으면서 M과 최대한 가까운 카드 3장의 합
"""

def blackjack():
    n,m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    max_lst = list()

    lst = sorted(lst)
    for i in range(len(lst)-1):
        left, right = i+1, len(lst)-1
        while left < right:
            sum = lst[i] + lst[left] + lst[right]
            if sum > m:
                right -= 1
            elif sum <= m:
                max_lst.append(sum)
                left += 1
        sum = max(max_lst)
    return sum

print(blackjack())
