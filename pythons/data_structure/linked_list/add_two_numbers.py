"""
002
두수의 덧셈
역순(reverse order)으로 저장된 연결리스트에 숫자를 더하기

[input]
1. (2 -> 4 -> 3) + (5 -> 6 -> 4) (l1 = [2,4,3], l2 = [5,6,4])
2. (0) + (0) (l1 = [0], l2 = [0])
3. l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]

[output]
1. 7 -> 0 -> 8 ([7, 0, 8])
2. [0]
3. [8,9,9,9,0,0,0,1]

[explanation]
342 + 465 = 807
"""

# Definition of singly-linked list
from dis import pretty_flags
from re import L
from typing import List


class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next

# 1
node1 = ListNode(2)
node2 = ListNode(4)
node1.next = node2
node3 = ListNode(3)
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node4.next = node5
node6 = ListNode(4)
node5.next = node6

# 2
node7 = ListNode(0)
node8 = ListNode(0)

# 3
node9_1 = ListNode(9)
node9_2 = ListNode(9)
node9_1.next = node9_2
node9_3 = ListNode(9)
node9_2.next = node9_3
node9_4 = ListNode(9)
node9_3.next = node9_4
node9_5 = ListNode(9)
node9_4.next = node9_5
node9_6 = ListNode(9)
node9_5.next = node9_6
node9_7 = ListNode(9)
node9_6.next = node9_7

node10_1 = ListNode(9)
node10_2 = ListNode(9)
node10_1.next = node10_2
node10_3 = ListNode(9)
node10_2.next = node10_3
node10_4 = ListNode(9)
node10_3.next = node10_4



class Solution:
    def reverseList(self, head: ListNode):
        """
        1단계 :  연결리스트 뒤집기 
        """
        node, prev = head, None 

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def tolist(self, node : ListNode):
        """
        node를 반복하여 값을 리스트에 추가한다.
        """
        lst = list()
        while node:
            list.append(node)
            node = node.next
        return lst
    
    def toReversedLinkedList(self, result:ListNode):
        """
        리스트를 연결리스트로 변경하는 함수
        """
        prev : ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumber(self, l1: ListNode, l2: ListNode): 
        """
        1. 링크드리스트 -> 문자열 "243", "564" 
        2. 계산 for 문 -> 342 + 465 = 807
        3. 다시 연결리스트 변환 -> [8,0,7]
        """
        a = self.tolist(self.reverseList(l1)) # 연결리스트 뒤집고 리스트화
        b = self.tolist(self.reverseList(l2)) 

        resultStr = int(''.join(str(e)) for e in a) + \
            int(''.join(str(e)) for e in b) # 한글자 씩 숫자형으로 변환

        return self.toReversedLinkedList(str(resultStr)) # 다시 연결리스트으로 변환

class Solution2:
    def addTwoNumber(self, l1: ListNode, l2: ListNode): 
        """
        ALU :전가산기 구현 방법 (Full Adder) 
        - ALU : CPU의 산술 논리 장치
        - A B S C.I C.O
          0 0 0 0    0
          0 1 1 0    1
          1 0 1 0    1
          1 1 0 0    0
          ...
        """
        root = head = ListNode(0)
        
        carry = 0
        # 두 입력의 합 계산  (2+5, 4+6 3+4)
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10) # divmod : 몫과 나머지를 구성된 튜플 리턴 (a // b , a % b)
            head.next = ListNode(val) # 7 0 1+7
            head = head.next # 8을 헤드로 
        
        return root.next

sol = Solution2()
sol.addTwoNumber(node1, node4)