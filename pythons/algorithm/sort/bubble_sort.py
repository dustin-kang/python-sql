"""
Bubble sort
"""

def bubblesort(data):
    for index in range(len(data)-1): # 전체 데이터 길이 - 1 (index)
        swap = False
        for index2 in range(len(data)-index-1): # 2회 로직 부터
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap = True
        if swap == False:
            break
        
    return data

# import random

# data_list = random.sample(range(100), 50)
# print(bubblesort(data_list))


"""
insertion sort
"""
def insertsort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1, 0, -1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else :
                break
    return data

# data_list = [5,3,7,9,4]
# print(insertsort(data_list))


"""
selection sort
"""
def selectionsort(data):
    for standard in range(len(data)-1):
        lowest = standard # 기준값 설정
        for index in range(standard+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[standard] = data[standard], data[lowest]
    return data

data_list = [5,3,7,9,4]
print(selectionsort(data_list))