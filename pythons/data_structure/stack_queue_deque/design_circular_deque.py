"""
[622]
원형 큐 디자인
- 문제 : 원형 큐를 디자인 하라


- 난이도 : ⭐️⭐️
- 시간복잡도 : O(n)


[EXAMPLE 1]
-Input-
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

-Output-
[null, true, true, true, false, 2, true, true, true, 4]

-Explanation-
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        """
        ### 데크 사이즈를 `k`로 지정하는 생성자
        - `k` : 데크의 사이즈
        - `head`, `tail` : 왼쪽 인덱스 역할, 오른쪽 인덱스 역할
        - `len` : 현재 길이 정보
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head


    def _add(self, node : ListNode, new: ListNode):
        """
        ### `_add()` 메소드 : 이중연결리스트에 신규 노드 삽입
        - 이미 있는 노드(n)를 지우고 그 사이에 새 노드(new)를 삽입
        """
        n = node.right
        node.right = new
        new.left, new.right =  node, n # new의 이전과 이후
        n.left = node 

    def _del(self, node: ListNode):
        """
        ### `_del()` 메소드 :  이중 연결리스트에 노드 삭제
        """
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        """
        ### 노드 추가 연산(처음)
        데크 처음에 아이템을 추가하고 성공할 경우 `True` 리턴
        """
        if self.len == self.k: # 만약 최대길이(k)와 현재 길이가 같은 경우 (도달시)
            return False
        self.len += 1
        self._add(self.head, ListNode(value)) # `_add()`메소드로  head 위치에 노드값을 삽입
        return True

    def insertLast(self, value: int) -> bool:
        """
        ### 노드 추가 연산(마지막)
        데크 마지막에 아이템을 추가하고 성공할 경우 `True` 리턴
        """
        if self.len == self.k: # 만약 최대길이(k)와 현재 길이가 같은 경우 (도달시)
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value)) # `_add()`메소드로  tail.left 위치에 노드값을 삽입
        return True

    def deleteFront(self) -> bool:
        """
        ### 노드 삭제 연산(처음)
        데크 처음에 아이템을 삭제하고 성공할 경우 `True` 리턴
        """        
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        """
        ### 노드 삭제 연산(마지막)
        데크 마지막에 아이템을 삭제하고 성공할 경우 `True` 리턴
        """       
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        """
        데크의 첫 번째 아이템을 가져온다. (만약 비어있을 경우 -1 리턴)
        """        
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        """
        데크의 마지막 번째 아이템을 가져온다. (만약 비어있을 경우 -1 리턴)
        """  
        return self.tail.left.val if self.len else -1      

    def isEmpty(self) -> bool:
        """
        데크가 비어있는지 여부
        """        
        return self.len == 0 

    def isFull(self) -> bool:
        """
        데크가 가득 차 있는지 여부
        """ 
        return self.len == self.k