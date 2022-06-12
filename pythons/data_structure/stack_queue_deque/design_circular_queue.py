"""
[622]
원형 큐 디자인
- 문제 : 원형 큐를 디자인 하라


- 난이도 : ⭐️⭐️
- 시간복잡도 : O(1)


[EXAMPLE 1]
-Input-
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

-Output-
[null, true, true, true, false, 3, true, true, true, 4]

-Explanation-
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k # 큐의 크기
        self.maxlen = k # k 값 =  최대길이
        self.p1 = 0 # front
        self.p2 = 0 # rear


    def enQueue(self, value: int) -> bool:
        """
        `enQueue()` : `rear` 포인터 이동 
        """
        if self.q[self.p2] is None: # 만약 해당 공간에 값이 없을 경우
            self.q[self.p2] = value # rear 포인터 p2 위치에 값을 넣는다.
            self.p2 = (self.p2 + 1) % self.maxlen # 포인터 위치가 전체 길이에 벗어나지 않게 함. (나머지 연산)
            return True
        else :
            return False # 공간이 꽉찬 상태거나 비정상적일 경우
        
        

    def deQueue(self) -> bool:
        """
        `dequeue()` : `front` 포인터 이동
        - 요소를 꺼내지 않고 삭제만 수행
        """
        if self.q[self.p1] is None: 
            return False
        else : 
            self.q[self.p1] = None # p1 위치에 None을 넣어 삭제 
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
        

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None

myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1)
myCircularQueue.enQueue(2)
myCircularQueue.enQueue(3)
myCircularQueue.enQueue(4)
myCircularQueue.Rear()
myCircularQueue.isFull()
myCircularQueue.deQueue()
myCircularQueue.enQueue(4)
myCircularQueue.Rear()