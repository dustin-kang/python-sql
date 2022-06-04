"""
206
역순 연결 리스트 2
M(left) 부터 N(right) 까지를 역순으로 만들어라.
- 인덱스 m 은 1부터 시작한다.

[난이도] ⭐️⭐️

[EXAMPLE 1]
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

[EXAMPLE 2]
Input: head = [5], left = 1, right = 1
Output: [5]

"""

# Difinition for Singly-Linked list


class ListNode:
    def __init__(self, val = 0, next = None ):
        self.val = val
        self.next = next

Node1 = ListNode(1)
Node2 = ListNode(2)
Node1.next = Node2
Node3 = ListNode(3)
Node2.next = Node3
Node4 = ListNode(4)
Node3.next = Node4
Node5 = ListNode(5)
Node4.next = Node5

Node55 = ListNode(5)

class Solution:
    def reverseBetween(self, head : ListNode, left : int, right : int):
        """
        root-[1]-[2]-3-4-5-6
        """
        # 1. 예외 처리
        if not head  or left == right:
            return head
        
        # 2. root - head 지정
        root = start = ListNode(None)
        root.next = head

        # 4. start, end 지정
        for _ in range(left - 1): # 처음부터 끝까지
            start = start.next # start = 1
        end = start.next # end = 2

        # 3. 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next


sol = Solution()
print(sol.reverseBetween(Node1, 2, 4))