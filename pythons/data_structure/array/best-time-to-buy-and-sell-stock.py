"""
121

주식을 사고 팔기 가장 좋은 시점
---
한번의 거래로 낼  수 있는 최대 이익을 산출하라


--input--
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

--output--
5 <- 1일 때  사서 6일 때  팔면 최대이익
0
"""
"""
1. 저점과 현재값과의 차이 계산
- 시간 복잡도 : O(n)
"""

prices = [7,1,5,3,6,4]
import sys
def stock1(prices):
    profit = 0
    min_prices = sys.maxsize

    for price in prices:
        min_prices = min(price, min_prices) # 현 가격 , 이전 최소값 비교 중 가장 최소값
        profit = max(profit, price - min_prices)    # 전 이윤, 현 이윤 비교중 가장 최대 값
    
    return profit

print(stock1(prices))


"""
2.브루트포스 계산
- 타임아웃
"""
def stock2(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(price[j]- price, max_price)
    return max_price

