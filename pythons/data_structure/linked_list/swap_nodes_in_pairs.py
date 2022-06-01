"""
24
페어의 노드 스왑(Swap)
연결리스트를 입력받아 페어 단위로 스왑해라

[input]
1. head = [1,2,3,4]
2. head = []
3. head = [1]

[output]
1. [2,1,4,3]
2. []
3. [1]

[explanation]
리스트의 노드 값을 수정하면 안됨.

"""

# Definition for Singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Node1 = ListNode(1)
Node2 = ListNode(2)
Node1.next = Node2
Node3 = ListNode(3)
Node2.next = Node3
Node4 = ListNode(4)
Node3.next = Node4
NodeX = ListNode()
Node1_1 = ListNode(1)

class Solution:
    def swapPairs(self, head : ListNode):
        """
        심플한 SWAP을 사용한 풀이 방법
        - 쉽게 풀이를 위해 변칙척으로 풀 수 있다.
        """
        node = head # 값이 바뀌지 않을 Node 변수 설정
        while head and head.next: # 반복
            head.val, head.next.val  = head.next.val, head.val # 단순 스왑
            head = head.next.next # 다다음 값을 헤더로 지정
        return node

    def swapPairs2(self, head : ListNode):
        """
        반복 구조로 스왑
        """
        root = prev = ListNode(None) # root = prev
        prev.next = head # prev = [ () - 1 - 2 - 3 - 4]
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b  = head.next # b = [2-3-4] // b = [4]
            head.next = b.next # head = [1 - 3 - 4] , 3-4를 붙인다. // head = [3]
            b.next = head # b = [2 - 1- 3 - 4] // b = [4-3]

            # prev가 b를 가리키도록 할당
            prev.next = b # prev =  ()-2-1-3-4  // prev = [1-4-3]

            # 다음번 비교를 위해 이동
            head = head.next # head = [3-4] // head = []
            prev = prev.next.next # prev = [1-3-4] // prev = [3]

        return root.next # root = [() - 2- 1- 4 -3]
    
    def swapPairs3(self, head : ListNode):
        """
        재귀 구조로 스왑
        - p -> head.next
        - p.next -> head
        1. p = 2-3-4 // head = 1--3-4
        2. p = 4 // head = 3-None (여기서 부터 백트래킹)
        3. p = 4-3
        4. p = 2-1-4-3

        백트래킹되면서 연결리스트의 페어가 스왑되는 구조
        """
        if head and head.next:
            p = head.next 
            # 스왑된 값을 리턴으로 받음
            head.next = self.swapPairs3(p.next) # p.next = 3-4
            p.next = head
            return p
        return head

sol = Solution()
print(sol.swapPairs3(Node1))
