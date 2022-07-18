def binary_search(data_list, value):
    low = 0
    high = len(data_list)
    
    while low <= high: # 반복
        middle = (low + high) // 2
        guess = data_list[middle]
        
        if guess == value: # 중간값이랑 같은 경우
            return guess
        if guess > value: # 중간값보다 큰 경우
            high = middle - 1 
        else : # 중간값보다 작은 경우
            low = middle + 1
    return None # 인덱스를 찾지 못한 경우


def binary_search2(data_list, value):
    if len(data_list) == 1 and value == data_list[0]: # 마지막 데이터인 경우 + 검색하는 숫자와 같은 경우
        return True
    if len(data_list) == 1 and value != data_list[0]: # 마지막 데이터인 경우 + 검색하는 숫자와 다른 경우
        return False
    if len(data_list) == 0: # 데이터가 없는 경우
        return False
    
    medium = len(data_list) // 2
    if value == data_list[medium]: # 검색하는 숫자가 중간값과 같은 경우
        return True
    else :
        if value > data_list[medium]: # 검색하는 숫자가 큰 경우
            return binary_search2(data_list[medium+1:], value)
        else : # 검색하는 숫자가 작은 경우
            return binary_search2(data_list[:medium], value)


import random
data_list = random.sample(range(100), 10)
data_list

data_list.sort()
binary_search(data_list, 72)
binary_search2(data_list, 72)