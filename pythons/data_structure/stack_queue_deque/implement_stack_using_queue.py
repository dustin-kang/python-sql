"""
[225]
큐를 이용한 스택 구현
- 문제 : 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
    push(x) : 요소 x 삽입
    pop() : 스택의 첫번째 요소 삭제
    top() :  스택의 첫번째 요소 가져오기
    empty() : 스택이 비어있는지 Boolean으로 리턴 (true : empty, flase : otherwise)


- 난이도 : ⭐️
- 시간복잡도: O(n)


[EXAMPLE 1]
-Input-
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

-Output-
[null, null, null, 2, 2, false]

-Explanation-
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x) #[2-1] + 3
        
        # 두번째 부터 요소 삽입 후 방금 삽입 한 요소를 맨 앞에 두는 상태로 정렬
        for _ in range(len(self.q) - 1): # 2번 진행
            self.q.append(self.q.popleft()) # [2-1-3] -> [1-3-2] -> [3-2-1]

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.top()
myStack.pop()
myStack.empty()