"""
- 201637011
Connecting Node using python
"""

class Node :
    def __init__(self, value, next = None): # Head Node's next -> None
        self.value = value # node value
        self.next = next # next location info 

class Linked_list:
    def __init__(self, value):
        self.head = Node(value) # First Head Node

    def add_node(self, value):
        """
        Connecting Node
        ----
        if : Head Node is None
        else : Head Node is not None
        """

        print("생성 전 헤드 노드 값 : ", head.value)
        print("생성 전 헤드 노드의 다음 위치 노드 값 : ", head.next)
        
        if self.head == None:
            self.head = Node(value)

        else:
            node = self.head # 첫번째 노드인 헤드를 'node'라는 변수에 저장
            while node.next :
                node = node.next
                print('print in while:', node.next)
            node.next = Node(value)
    
    def del_node(self,value):
        """
        Deleting Node
        ----
        if : head node is None
        elif : head node is delete node
        else : next node is delete node
        """
        if self.head == None:
           return # Noting return

        elif self.head.value == value: # delete value is head node
            delete = self.head
            self.head = self.head.next
            return delete.value
        else : # anyone node
            node = self.head
            while node.next:
                if node.next.value == value:
                    delete = node.next
                    node.next = node.next.next
                    return delete.value
                else :
                    node  = node.next
    def ord_desc(self):
        """
        Node print
        """
        node = self.head
        while node :
            print(node.value)
            node = node.next
    def search_node(self, value):
        """
        search node
        value == node.value
        """
        node = self.head
        while node :
            if node.value == value:
                return node
            else : 
                node = node.next

head = Node(5)
Linked_list.add_node(10)

print("헤드 노드의 값",head.value)
print("헤드 노드의 다음 위치 노드의 값", head.next.value)

# Connecting Node

node1 = Node(3)
node2 = Node(4)
node3 = Node(5)
node4  = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4

# Node executing script
node = node1
while node1:
    print(node.value)
    node = node.next

# Node print test
Linked_list = Linked_list(0)
Linked_list.ord_desc()

# Node add test
for value in range(1, 10):
    Linked_list.add_node(value)
Linked_list.ord_desc()

# Node delete test
print("-TEST 1- \n")
Linked_list = Linked_list(0) # first value
Linked_list.del_node(0)
Linked_list.del_node(0)
Linked_list.ord_desc()

print("-TEST 2- \n")
Linked_list = Linked_list(0) # first value
for value in range(1,5):
    Linked_list.add_node(1,5)
Linked_list.del_node(1)
Linked_list.ord_desc()

# reset node
linkedlist = Linked_list(0)

# searching node test
node = Linked_list.search_node(4)
print(node.value)
print(node.next.value)