"""
234
연결 리스트가 팰린 드롬인지 확인하는 문제
? 팰린드롬(회문) : 앞뒤가 똑같은 단어 또는 문장을 말함.

[input]
1. 1 -> 2
2. 1 -> 2 -> 2 -> 1
[output]
1. false
2. true
"""
import collections


# Definition for singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# # 1
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(2)
node2.next = node3
node4 = ListNode(1)
node3.next = node4

# # 2
# node1 = ListNode(1)
# node2 = ListNode(2)
# node1.next = node2



class Solution:
    def ispalindrome(self, head: ListNode):
        """
        # 1. 파이썬 리스트로 변환하기
        - pop(0)에서 한칸씩 시프팅 되면서 O(n)이 발생함.
        - 2856 ms
        """
        q = list()
        
        # 우선 Head Node가 없는 경우 작성
        if not head:
            return True

        while head:
            q.append(head.val)
            head = head.next
        
        # 팰린드롬

        while len(q) > 1:
            if q.pop() != q.pop(0):
                return False


        return True 

    def isPalindrome_deque(self, head: ListNode):
        """
        # 2. 데크를 활용한 방법
        - 이중 연결 리스트 : 그냥 리스트를 사용하면 타임아웃이 발생할 수 있기 때문이다.
            - 이 방식은 O(1)의 방식이다.
        - 1546 ms
        """
        q = collections.deque()

        if not head:
            return True

        while head:
            q.append(head.val)
            head = head.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True

    def isPalindrome_runner(self, head: ListNode):
        """
        # 3. 런너(Runner) 기법을 사용한 풀이 방법
        - 1203 ms
        - fast : fast.next.next (두칸씩)
        - slow : slow.next (한칸씩)
        - rev(역순)
        """
        rev = None
        slow = fast = head

        while fast and fast.next: 
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


solution = Solution()
# print(solution.ispalindrome(node1))
# print(solution.isPalindrome_deque(node1))
print(solution.isPalindrome_runner(node1))
