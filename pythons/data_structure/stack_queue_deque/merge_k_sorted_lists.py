"""
[023]
k개 정렬 리스트 병합
- 문제 : k개의 정렬된 리스트를 1개의 리스트로 병합하라.

- 난이도 : ⭐️
    - 우선 순위를 아는 경우에 한정.
- 시간복잡도: O(n)


[EXAMPLE 1]
-Input-
lists = [[1,4,5],[1,3,4],[2,6]]

-Output-
[1,1,2,3,4,4,5,6]

-Explanation-
The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

[EXAMPLE 2]
-Input-
lists = []

-Output-
[]

[EXAMPLE 3]
-Input-
lists = [[]]

-Output-
[]
"""

# Definition for Singly linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

Node1 = ListNode(1)
Node4 = ListNode(4)
Node1.next = Node4
Node5 = ListNode(5)
Node4.next = Node5

Node2_1 = ListNode(1)
Node2_3 = ListNode(3)
Node2_1.next = Node2_3
Node2_4 = ListNode(4)
Node2_3.next = Node2_4

Node3_2 = ListNode(2)
Node3_6 = ListNode(6)
Node3_2.next = Node3_6

lst1 = [Node1, Node2_1, Node3_2]

lst2 = []

lst3 = [[]]

import heapq
from queue import PriorityQueue # 힙 큐 모듈

class Solution:
    def mergeKLists(self, lists):
        """
        ### 우선순위 큐를 이용한 리스트 병합
        - `heapq` 모듈을 사용하여 `lst.val`이 작은 순서대로 pop()을 할 수 있다.
        -  첫번째 연결리스트와 두번째 연결리스트는 처음 노드가 1이므로 (중복되므로) list.val[i]로 수정
        - `heappush`를 통해 힙에 각 연결리스트의 루트를 저장하게 된다.
        - `heappop`을 통해 가장 작은 노드의 연결리스트 부터 나오게 된다.
        """
        root = result = ListNode(None)
        heap = [] # 연결리스트의 루트를 저장

        # 각 연결리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) # [(1,0, 연결리스트1), (1,1, 연결리스트2), (2,2, 연결리스트3)]

        # 힙 추출 
        while heap: # 힙이 빌때까지 반복
            node = heapq.heappop(heap)
            idx = node[1] # i
            result.next = node[2] # 연결리스트
            
            # 추출한 연결리스트의 그 다음 노드는 다시 힙에 추가
            result = result.next 
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next)) # [..., (4,0, 다음연결리스트1)]
        
        return root.next


solution = Solution
solution.mergeKLists(solution, lst1)


