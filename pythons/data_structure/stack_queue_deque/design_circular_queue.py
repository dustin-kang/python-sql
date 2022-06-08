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