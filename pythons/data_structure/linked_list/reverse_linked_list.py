"""
206
역순 연결 리스트
연결리스트를 뒤집어라

[input]
1. head = [1,2,3,4,5]
2. head = [1,2]
2. head = []

[output]
1. [5,4,3,2,1]
2. [2,1]
3. []

"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 1
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5

# 2
node2_1 = ListNode(1)
node2_2 = ListNode(2)
node2_1.next = node2_2

# 3
nodeX = ListNode()


class Solution:
    def reverseList(self, head : ListNode):
        """
        리스트로 만든다.
        역순으로 돌린다.
        다시 연결리스트로 만든다.
        """
        q = list()
        prev : ListNode() = None
        
        # 연결리스트 -> 리스트
        while head is not None:
            q.append(head.val)
            head = head.next

        # 리스트를 연결리스트로 만들고 뒤집는다.
        while len(q) > 0:
            node = ListNode(q.pop(0)) # 리스트를 연결리스트로 만듬
            node.next = prev # 역순으로 돌아가기 1
            prev = node # 역순으로 돌아가기 2

        return node

    def reverseList2(seld, head : ListNode):
        """
        이해하기 어려웠던 재귀 함수 풀이법
        """
        def reverse(node : ListNode, prev: ListNode = None):
            if not node: # 재귀 결과
                return prev # prev : 뒤집힌 노드의 첫번째 노드
            next, node.next = node.next, next # 다음 노드(next), 현재노드(node) 재귀 호출
            return reverse(next, node)
        
        return reverse(head)

    def reverseList3(self, head : ListNode):
        """
        반복 구조로 뒤집는 풀이법
        """
        node, prev = head, None
        # node : 1(head)
        # prev : None

        while node: # Node 가 None 될때 까지
            next, node.next = node.next, prev
            """
            node : 2[1] -> 1[None]
            prev : 1[None]
            next : 3[4] 4[5] 5[None]
            """
            prev, node = node, next
            """
            node : 3[4] 4[5] 5[None]
            prev : 2[1] -> 1[None]
            next : 3[4] 4[5] 5[None]
            """
            # prev-> node.next
            # node -> prev
        return prev



solution = Solution()
# print(solution.reverseList(nodeX))
print(solution.reverseList3(node1))

