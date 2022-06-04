"""
[225]
큐를 이용한 스택 구현
- 문제 : 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
    push(x) : 요소 x 삽입
    pop() : 스택의 첫번째 요소 삭제
    top() :  스택의 첫번째 요소 가져오기
    empty() : 스택이 비어있는지 Boolean으로 리턴 (true : empty, flase : otherwise)


- 난이도 : ⭐️



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