"""
[232]
스택을 이용한 큐 구현
- 문제 : 스택를 이용해 다음 연산을 지원하는 큐을 구현하라.
    push(x) : 요소 x를 큐 마지막에 삽입
    pop() : 큐의 첫번째 요소 삭제
    peek() :  큐의 첫번째 요소 조회
    empty() : 스택이 비어있는지 Boolean으로 리턴 (true : empty, flase : otherwise)


- 난이도 : ⭐️
- 시간복잡도 : O(1)


[EXAMPLE 1]
-Input-
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

-Output-
[null, null, null, 1, 1, false]

-Explanation-
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
"""

class MyQueue:

    def __init__(self):
        self.rear = []
        self.front = []

    def push(self, x: int) -> None:
        self.rear.append(x)

    def pop(self) -> int:
        self.peek()
        return self.front.pop()

    def peek(self) -> int:
        if not self.front:
            while self.rear:
                self.front.append(self.rear.pop())
        return self.front[-1]
        

    def empty(self) -> bool:
        return self.rear == [] and self.front == []


# Your MyQueue object(myqueue) will be instantiated and called as such:
myqueue = MyQueue()
myqueue.push(1)
myqueue.push(2)
myqueue.peek()
myqueue.pop()
myqueue.empty()