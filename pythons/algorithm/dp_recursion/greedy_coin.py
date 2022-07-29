# 1. 동전 리스트 만들기

coins = [10, 100, 50, 500, 1000]
coins.sort(reverse=True) # 500부터 정렬
print(coins)

# 2. 동전 알고리즘 만들기

def counting_coin(value, coins):
    """
    1000이 가장 최적으로 생각
    그다음 최적.. 그다음 최적
    """
    total_coin_count = 0 # 전체 동전 갯수
    details = list() # 동전 디테일 리스트
    
    for coin in coins: # 500 부터 반복
        coin_count = value // coin # 가격 // 동전
        total_coin_count += coin_count # 전체 동전 갯수에 동전 갯수 추가
        value -= coin_count * coin # 동전 갯수 * 동전 
        details.append([coin, coin_count]) # [동전, 동전 갯수]
    return total_coin_count, details


counting_coin(3990, coins)