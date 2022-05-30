"""
021
두 정렬 리스트의 병합
정렬되어 있는 두 연결 리스트를 합쳐라

[input]
1. [1-2-4], [1-3-4] (list1 = [1,2,4], list2 = [1,3,4])
2. [], [] (list1 = [], list2 = [])
3. [], [0] (list1 = [], list2 = [0])

[output]
1. [1-1-2-3-4-4]
2. []
3. [0]
"""

# Definition of singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

Node1 = ListNode(1)
Node2 = ListNode(2)
Node1.next = Node2
Node3 = ListNode(4)
Node2.next = Node3

Node4 = ListNode(1)
Node5 = ListNode(3)
Node4.next = Node5
Node6 = ListNode(4)
Node5.next = Node6

Node0 = ListNode(0)

NodeX = ListNode(None)

class Solution:
    def mergeTwoLists(self, list1 : ListNode, list2: ListNode):
        """
        l2 보다 크면 swap
        """
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

    def mergeTwoLists2(self, l1 : ListNode, l2 : ListNode):
            cur = result = ListNode()  # 새로운 연결리스트

            while l1 and l2: # 두 리스트가 있는 경우
                if l1.val > l2.val: # l2 보다 l1이 큰 경우
                    cur.next = l1 # cur 연결리스트에 이어 붙이기
                    l1, cur = l1.next, l1 # 다음 정보 연결하기
                else : # 그게 아닌 경우
                    cur.next = l2
                    l2, cur = l2.next, l2

            if l1 or l2: # 둘 중 하나만 있는 경우
                cur.next = l1 if l1 else l2

            return result.next # 이어 붙인 시점 부터


solution = Solution()
print(solution.mergeTwoLists2(Node1, Node4))
