"""
[706]
해시 맵  디자인
- 문제 : 다음의 기능을 만족하는 해시맵을 디자인하라.


- 난이도 : ⭐️
- 시간복잡도 : 


[EXAMPLE 1]
-Input-
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

-output-
[null, null, null, 1, -1, null, 1, null, -1]


-explanation-
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

"""
import collections


class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    """
    개별 체이닝 방법(연결리스트 형식 비슷)으로 구현한 해시 테이블
    - `put(key, value)` : 키, 값을 해시맵에 삽입, 이미 있으면 업데이트
    - `get(key)` : 키에 해당하는 값을 조회, 존재하지 않으면 -1
    - `remove(key)` : 키에 해당하는 키, 값을 해시맵에서 삭제
    """
    def __init__(self):
        """
        ### 초기화
        `size` = 기본사이즈로 1000개 정도 적당히 설정
        `table`
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        ### 삽입 메소드
        `key, value` : 삽입할 키와 값
        `index` : 모듈로 연산을 통한 해싱 방식을 한 해싱 결과
        - 해당 인덱스에 노드가 존재하는 경우 OR 존재하지 않은 경우 (해시충돌 유무)
        """
        index = key % self.size
        # 만약 해당 인덱스에 아무것도 없을 경우
        #  존재하지 않는 경우 빈 노드 생성
        if self.table[index].value is None: # defaultdict이기 때문에 `value is None` 함
            self.table[index] = ListNode(key, value) # 키 값 삽입 하고 바로 종료
            return

        # 해당 인덱스에 노드가 존재하는 경우 (해시 충돌)
        p = self.table[index]
        while p:
            if p.key == key: # 이미 키가 존재하는 경우
                p.value = value # 값 업데이트
                return
            if p.next is None: # 후자가 없다면
                break # BREAK!
            p = p.next
        p.next = ListNode(key, value) # 새로운 노드 생성 및 연결
        

    def get(self, key: int) -> int:
        """
        ### 조회 메소드
        `key` : 조회할 키
        `index` : 모듈로 연산을 통한 해싱 방식을 한 해싱 결과

        - `key`를 통해 조회하며  `value`를 리턴한다. 없으면 `-1`
        """
        index = key % self.size # 모듈 연산으로 인덱스 결정
        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key: # 키값이 존재한다면 
                return p.value # 값 뱉기
            p = p.next # 다음으로 돌리기
        return -1 # 값을 찾지 못하면 -1 리턴


    def remove(self, key: int) -> None:
        """
        ### 제거 메소드
        `key` : 제거할 키
        `index` : 모듈로 연산을 통한 해싱 방식을 한 해싱 결과
        """
        index = key % self.size # 모듈 연산으로 인덱스 결정
        if self.table[index].value is None:
            return -1

        # 인덱스의 첫번째 노드일때, 삭제 처리
        p = self.table[index]
        if p.key == key: # 제거할 키 값이 존재한다면
            self.table[index] = ListNode() if p.next is None else p.next
            # ListNode()로 초기상태만들기 , self.table[index] = None (X)
            return

        # 연결리스트 노드 삭제
        prev = p # 이전노드
        while p:
            if p.key == key: # 일치하는 노드 발생시
                prev.next = p.next # 연결고리를 끊어버림.
                return
            prev, p = p, p.next
        


obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
param1 = obj.get(1)
param2 = obj.get(3)
obj.put(2,1)
param3 = obj.get(2)
obj.remove(2)
param4 = obj.get(2)