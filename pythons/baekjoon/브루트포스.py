"""
브루트 포스
- 블랙잭 (2798)
- 분해합 (2231)
- 덩치 (7568)
- 체스판 다시 칠하기 (1018)
- 영화 감독 숌 (1436)
"""
import sys
from tkinter import N
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

# print(blackjack())


"""
2231
분해합

- 분해합  : 어떤 자연수가 있을 경우 각 자리수의 합을 의미 (245의 분해합 : 245 + 2 + 4 + 5 = 256)
- 생성자 : 어떤 자연수의 분해합이 N인 경우 자연수를 N의 생성자라 칭함  (245가 256의 생성자)

자연수 N이 주어졌을 경우, N의 가장 작은 생성자를 구하는 프로그램 작성


[입력]
216

[출력]
198

[설명]
없는 경우 0을 출력
"""
class Decompos:
    def __init__(self):
        pass

    def desum(self, n):
        """
        분해합 구하기
        """
        s = n

        numstr = str(n)
        for i in range(len(numstr)):
            s = s + int(numstr[i])
        return s

    def findCon(self, m):
        """
        생성자 확인
        """
        for i in range(m):
            if m == self.desum(i) : 
                return i
        return 0

# decom = Decompos()
# n = int(input())
# decom.findCon(n)


def decom2():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        a = list(map(int, str(i))) # 1~ 그 수까지 리스트에 넣기 (1, 9 , 8)
        result = i + sum(a) #
        if result == n :
            print(i)
            break
        
        if i == n : # 생성자가 없는 경우
            print(0)

print(decom2())
