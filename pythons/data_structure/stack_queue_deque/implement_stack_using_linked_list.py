"""
- 201637011
연결리스트를 이용한 스택 ADT 구현
"""


class ListNode:
    def __init__(self, val = 0, next = None):
        """
        - 연결리스트의 값은 val로 지정
        - 연결리스트의 다음 노드 포인터를 next로 정의
        """
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        """
        ### 연결리스트 요소 추가
        - 가장 마지막값 self.top을 next로 설정
        """
        new_node = ListNode(val, self.top) # 신규 노드 생성
        self.top = new_node # 신규노드를 최상단에 삽입
        return new_node.val # 신규노드 리턴

    
    def pop(self):
        """
        ### 연결리스트 요소 삭제
        - 가장 마지막 값을 val로 지정하고
        - 다음 값을 다시 top으로 변경
        """
        if self.top is not None:
            # TOP이 비어 있지 않은 경우
            popped_data = self.top # 최상단 노드를 삭제할 노드로 지정
            self.top = popped_data.next # 최상단 다음 노드를 최상단 노드로 지정
            return popped_data.val # 삭제할 노드 리턴


    def ord_desc(self):
        """
        연결리스트 노드 출력
        """
        node = self.top
        while node:
            print(node.val)
            node = node.next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        """
        ### 연결리스트에 값을 삽입하는 함수
        """
        new_node = ListNode(val, next=None)
        
        if self.rear is None:
            # 큐가 비어있는 경우
            self.front = new_node
            self.rear = new_node
        else : 
            # 하나라도 채워있는 경우
            self.rear.next = new_node 
            self.rear = new_node
        return new_node.val

    def dequeue(self):
        """
        ### 연결리스트에 값을 삭제하는 경우
        """
        if self.front is not None:
            # 큐가 비어있지 않은 경우
            old_front = self.front
            self.front = old_front.next
        if self.front is None:
            # 큐가 비어있는 경우
            self.rear = None 
        return old_front.val # 구 프론트 제거

    def ord_desc(self):
        node = self.front
        while node:
            print(node.val)
            node = node.next

stack = Stack()
stack.pop()
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(3)
stack.ord_desc()
stack.pop()
stack.ord_desc()


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.ord_desc()
queue.dequeue()
queue.dequeue()
queue.ord_desc()