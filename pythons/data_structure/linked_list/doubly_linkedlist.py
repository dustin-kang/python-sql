class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init(self, data):
        self.head = Node(data)
        self.tail = self.head # 양쪽 구조로 되어있기 때문

    def insert(self, data):
        """
        # 데이터 추가하기
        - `data` : 추가할 데이터
        """
        # 예외 코드
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else: 
            while node.next: # next 노드가 존재하는 경우
                node = node.next
            # next 노드가 존재하지 않은 마지막 노드인 경우
            new_node = Node(data) # 새 노드 변수 지정
            node.next = new_node  # Node -> NEW
            new_node.prev = node # Node -> NEW (객체간 연결)
            self.tail = new_node # NEW(TAIL)

    def desc(self):
        """
        # 모든 데이터 출력
        """
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def search_from_head(self, data):
        """
        # 헤더 부터 특정 데이터 찾기
        """
        # 예외 코드
        if self.head = None:
            return False
        # 헤더가 있는 경우
        node = self.head
        while node:
            if node.data == data:
                return node
            else :
                node = node.next
        return False

    def search_from_tail(self, data):
        """
        # 테일 부터 특정 데이터 찾기
        """
        # 예외 코드
        if self.head = None:
            return False
        # 테일이 있는 경우
        node = self.tail
        while node:
            if node.data == data:
                return node
            else :
                node = node.prev # 뒤에서 앞으로
        return False
    
    def insert_before(self, data, before_data):
        """
        특정 데이터(`before_data`) 앞에 데이터 삽입하기
        - 뒤에서 앞으로
        """
        # 예외 코드
        if self.head = None
            self.head = Node(data)
            return True
        else :
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None: # 찾는 노드가 없는 경우
                    return False 
            # 찾는 노드가 있는 경우
            new_node = Node(data) # 새 데이터 변수 지정
            before_new = node.prev # 기존 앞 노드 변수 지정
            before_new.next = new_node # 기존 앞 노드 -> new_node
            new_node.next = node # new_node -> node
            return True

    def insert_after(self, data, after_data):
        """
        특정 데이터(`after_data`) 뒤에 데이터 삽입하기
        - 앞에서 뒤로
        """
        # 예외 코드
        if self.head = None
            self.head = Node(data)
            return True
        else :
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None: # 찾는 노드가 없는 경우
                    return False 
            # 찾는 노드가 있는 경우
            new_node = Node(data) # 새 데이터 변수 지정
            after_new = node.next # 기존 뒤 노드 변수 지정
            new_node.next = after_new # new_node -> after_new
            new_node.prev = node # node -> new_node
            node.next = new_node # node -> new_node
            if new_node.next == None: # 마지막 노드일 경우
                self.tail = new_node
            return True    

linklist = DoublyLinkedList(0)
for data in range(1, 10):
    linklist.insert(data)

linklist.desc()

linklist.insert_after(1.5, 1)

linklist.search_from_tail(3)