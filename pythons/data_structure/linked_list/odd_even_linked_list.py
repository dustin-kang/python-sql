"""
328
홀짝 연결 리스트
연결리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라.

- 공간 복잡도 : O(1)
- 시간 복잡도 : O(n)

[Example 1]
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

[Example 2]
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""

# Definition for Signly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 1
Node1_1 = ListNode(1)
Node1_2 = ListNode(2)
Node1_1.next = Node1_2
Node1_3 = ListNode(3)
Node1_2.next = Node1_3
Node1_4 = ListNode(4)
Node1_3.next = Node1_4
Node1_5 = ListNode(5)
Node1_4.next = Node1_5
Node1_6 = ListNode(6)
Node1_5.next = Node1_6
Node1_7 = ListNode(7)
Node1_6.next = Node1_7
Node1_8 = ListNode(8)
Node1_7.next = Node1_8

# 2
Node2_1 = ListNode(2)
Node2_2 = ListNode(1)
Node2_1.next = Node2_2
Node2_3 = ListNode(3)
Node2_2.next = Node2_3
Node2_4 = ListNode(5)
Node2_3.next = Node2_4
Node2_5 = ListNode(6)
Node2_4.next = Node2_5
Node2_6 = ListNode(4)
Node2_5.next = Node2_6
Node2_7 = ListNode(7)
Node2_6.next = Node2_7


class Solution:
    def oddEvenList(self, head : ListNode):
        
        node, odd = head, ListNode(0)
        prev = odd

        while head and head.next:
            odd.next, head.next = head.next, head.next.next
            odd = odd.next
            if head.next == None:
                break
            head = head.next
        
        odd.next = None
        head.next = prev.next

        return node
    def oddEvenList2(self, head : ListNode):
        """
        반복 구조로 홀짝 처리
        """
        # 예외 처리
        if head is None:
            return None
        
        # 변수 설정
        odd = head # 홀수
        even = head.next # 짝수
        even_head =  head.next

        # 반복하면서 홀수 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 마지막 연결 (홀수 노드 마지막 --연결-- 짝수 헤드)
        odd.next = even_head
        return head

sol = Solution()
print(sol.oddEvenList2(Node1_1))
print(sol.oddEvenList2(Node2_1))