hash_table = list([0 for i in range(8)])

def get_key(data):
    """
    ### 1. 데이터를 Hash Key 형식으로 바꿉니다.
    `index_key`
    """
    return hash(data)

def hash_func(key):
    """
    ### 2. 해시 함수
    해시키 - [해시함수] - 해시 주소(값)
    `hash_address`
    """
    return key % 8

def save_data(data, value):
    """
    ### 3. 값을 저장할 때
    `[index_key, hash_address]`
    `[ <hash_table>
        [ <hash_address>
            [ <index>
                index_key,
                value
            ]
        ],
        0,
        0
    ]
    """
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address] != 0: # 해시 테이블에 주소가 존재할 경우
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key: # 동일한 인덱스 키 일 경우
                hash_table[hash_address][index][1] = value # 다음 값 저장
                return
        hash_table[hash_address].append([index_key, value]) # 동일한 인덱스 키가 아닌 경우 그냥 추가
    else: # 해시 테이블 주소가 존재하지 않은 경우
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    """
    ### 4. 값을 가져올 때
    `[index_key, hash_address]`
    """
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0: # 해시 테이블 주소가 존재하는 경우
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else : # 해시 테이블 주소가 존재하지 않은 경우 -> 읽을 이유가 없음
        return None

print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)

save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')