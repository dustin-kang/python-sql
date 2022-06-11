"""
- 201637011
Making Hash Function Using Python
"""
bytes_representation = "hello".encode()

for byte in bytes_representation:
    sum += byte # 각 글자 바이트마다 총합을 구함

print(sum)


def my_hashing_func(str, list_size):
    """
    해시 함수 만들기
    - Parameter  : 문자열, 리스트 길이
    - `char`의 바이트의 합계 % 리스트(해시테이블) 공간의 크기
    """
    bytes_representation = str.encode()
    sum = 0
    for byte in bytes_representation:
        sum += byte # 각 글자 바이트마다 총합을 구함

    print('sum:', sum) # 글자 바이트 수의 합계
    print('list_size', list_size) # 리스트의 길이
    print('sum%list_size:', sum % list_size) # 들어갈 공간 인덱스
    return sum % list_size


my_list = [None] * 5
# [None, None, None, None, None] 리스트 초기화

my_list[my_hashing_func("aqua", len(my_list))] = "#00FFFF"

my_list

