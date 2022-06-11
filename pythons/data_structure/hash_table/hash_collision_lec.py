"""
- 201637011
Making Hash Collision Using Python
"""

# 해시 함수 및 테이블 만들어 충돌 발생시키기

hashtable = [None] * 5 # 해시 테이블
print(hashtable) # key

def hash_function(key):
    """
    해시 함수 (키 값)
    - 키 % 해시테이블의 길이
    - 해시 키 출력
    """
    return key % len(hashtable)

print(hash_function(10)) # 해시 충돌 발생 
print(hash_function(20)) # 해시 충돌 발생
print(hash_function(31))


# 해시 테이블에 데이터 삽입하기

def insert_hash(hashtable, key, value):
    """
    해시 테이블에 해시 키를 이용한 데이터 삽입
    """
    hash_key = hash_function(key)
    hashtable[hash_key] = value # 해시 함수를 통해 받은 해시키 -> 값으로 변환

insert_hash(hashtable, 10, 'A') # 키(10)를 해시함수(hash_function)를 통해 해시(0)로 바꿔 0번째 인덱스에 값('A') 삽입
print(hashtable)

insert_hash(hashtable, 23, 'B')   # 3번째 인덱스에 B가 삽입됨
print(hashtable)

insert_hash(hashtable, 20, 'Collision') # 20이라는 키를 해시키로 바꿔 0번째 인덱스에 Collision을 저장
print(hashtable) # 💥충돌💥


"""
체이닝을 이용하여 해시 충돌 보완하기
"""

# 해시 테이블 만들기
chain_hash_table = [[] for _ in range(10)] # 10의 길이로 테스트 (0~9), 10개 인덱스
print(chain_hash_table)


# 해시 함수 만들기
def chain_hash_func(key):
  return key % len(chain_hash_table)

print(chain_hash_func(10)) 
print(chain_hash_func(20)) 
print(chain_hash_func(25))

# extend()를 활용해 키 값 쌍을 해시 테이블에 삽입하기

def chain_insert_func(chain_hash_table, key, value):
    """
    이전과의 차이점
    - `.extend()` 메소드를 사용하여 충돌을 막는다. 
    """
    hash_key = chain_hash_func(key) # 해시함수 (키 -> 해시키)
    chain_hash_table[hash_key].extend(value)  # 해시테이블의 값을 넣는다.

chain_insert_func(chain_hash_table, 10, 'A')
print (chain_hash_table)

chain_insert_func(chain_hash_table, 25, 'B')    # 5번째 인덱스에 B가 삽입된다.
print (chain_hash_table)

chain_insert_func(chain_hash_table, 20, 'C')    
print (chain_hash_table)

# [['A', 'C'], [], [], [], [], ['B'], [], [], [], []]