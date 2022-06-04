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
        new_node = ListNode(val, self.top)
        self.top = new_node
        return new_node.val

    
    def pop(self):
        """
        ### 연결리스트 요소 삭제
        - 가장 마지막 값을 val로 지정하고
        - 다음 값을 다시 top으로 변경
        """
        if self.top is not None:
            # TOP이 비어 있지 않은 경우
            popped_data = self.top
            self.top = popped_data.next
            return popped_data.val


    def ord_desc(self):
        """
        연결리스트 노드 출력
        """
        node = self.top
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