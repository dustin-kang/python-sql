class Node:
    """
    노드 클래스 만들기
    """
    def __init__(self,value):
        self.value = value
        self.left = None # 왼쪽 노드
        self.right = None # 오른쪽 노드


class BST:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        """
        ### 이진트리 값 `insert`하기
        1. 순회할 노드 선정하여 순회(`while`) 하기
        2-A. 추가할 값이 현재 노드보다 작은경우 (왼쪽으로)
            - 왼쪽 노드가 있는 경우
            - 왼쪽 노드가 없는 경우
        2-B. 추가할 값이 현재 노드보다 큰 경우 (오른쪽으로)
            - 오른쪽 노드가 있는 경우
            - 오른쪽 노드가 없는 경우
        """
        self.current_node = self.head # 우선 순회할 노드 선정
        while True : # 순회
            if value < self.current_node.value: # 값이 current_node보다 작은 경우 (왼쪽)
                if self.current_node.left != None: # 왼쪽 노드가 있다.
                    self.current_node = self.current_node.left # 왼쪽 노드를 현재노드로 설정하고 순회
                else :
                    self.current_node.left = Node(value)
                    break
            else :
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else :
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        """
        ### 이진트리 값 찾기 `search`
        1. 현재 노드를 순회하여 현재 노드 인지, 작은 노드 인지, 큰 노드인지로 순회
        """
        self.current_node = self.head
        while self.current_node: # 현재 노드를 순회
            if self.current_node.value == value: # 순회할 노드가 찾는 노드라면
                return True # 바로 True
            elif value < self.current_node.value: # 순회할 노드보다 작은 경우
                self.current_node = self.current_node.left 
            else : # 순회할 노드보다 큰 경우
                self.current_node = self.current_node.right
        return False    # 아무리 찾아도 없는 경우

    def delete(self, value):
        """
        ## 이진트리 값 삭제하기
        0. 먼저 순회할 노드 설정
        ### Case 1. Current_node의 자식 노드가 없는 경우
            1-1. Current Node가 왼쪽
            1-2. Current Node가 오른쪽
        ### Case 2. Current_node의 자식 노드가 한 개인 경우
            2-1. Current_node의 자식 노드가 왼쪽
                - 삭제 값이 부모보다 크다 (Current => 오른쪽)
                - 삭제 값이 부모보다 작다 (Current => 왼쪽)
            2-2. Current_node의 자식 노드가 오른쪽
                - 삭제 값이 부모보다 크다 (Current => 오른쪽)
                - 삭제 값이 부모보다 작다 (Current => 왼쪽)
        ### Case 3. Current_node의 자식 노드가 두 개인 경우
        3-1. 삭제 할 값이 부모보다 작은 경우 (왼쪽)
            - 왼쪽에 있는 삭제할 노드의 오른쪽 자식 중 Child Node가 없는 경우
            - 왼쪽에 있는 삭제할 노드의 오른쪽 자식 중 Child Node가 오른쪽에 있는 경우 (왼쪽에는 해당 노드보다 더 작은 노드가 있다는 얘기임으로 없음)
        3-2. 삭제 할 값이 부모보다 큰 경우 (오른쪽)
            - 오른쪽에 있는 삭제할 노드의 오른쪽 자식 중 Child Node가 없는 경우
            - 오른쪽에 있는 삭제할 노드의 오른쪽 자식 중 Child Node가 오른쪽에 있는 경우 (왼쪽에는 해당 노드보다 더 작은 노드가 있다는 얘기임으로 없음)
        """
        # 삭제할 노드 탐색
        searched = False
        self.current_node = self.head # 순회할 노드 선정
        self.parent = self.head # 부모노드 선정

        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value: # 현재 노드값보다 작은 경우 (왼쪽)
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else :  # 현재 노드값보다 큰 경우 (오른쪽)
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched = False:
            return False

        # Case 1. Current Node의 자식 노드가 없는 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value: # 1-1. Current Node가 왼쪽의 경우 (작은 경우)
                self.parent.left = None # 그냥 Edge 삭제
            else : # 1-2. Current Node가 오른쪽인 경우 (큰 경우)
                self.parent.right = None # 그냥 Edge 삭제
            del self.current_node # Node 삭제

        # Case 2. Current Node의 자식 노드가 한 개인 경우
        if self.current_node.left != None and self.current_node.right == None: # 2-1. Current 노드의 자식노드가 왼쪽에만 있는 경우
            if value < self.parent.value: # 삭제할 값이 부모노드 보다 큰 경우 (Current가 오른쪽)
                self.parent.left = self.current_node.left
            else : # Current가 왼쪽
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None: # 2-1. Current 노드의 자식노드가 오른쪽에만 있는 경우
            if value < self.parent.value: # 삭제할 값이 부모노드 보다 큰 경우 (Current가 오른쪽)
                self.parent.left = self.current_node.right
            else : # Current가 왼쪽
                self.parent.right = self.current_node.right
        
        # Case 3. Current Node의 자식 노드가 두 개인 경우
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value : # 3-1. 삭제할 값이 부모 값보다 작은 경우 (왼쪽)
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left != None: # Change Node의 Left가 없을 때 까지 순회
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None: # Change Node의 Right 값이 있을 경우
                    self.change_node_parent.left = self.change_node.right # Change Node의 자식 노드를 Change Node(CN.P.l)랑 바꾼다.
                else : # 없는 경우
                    self.change_node_parent.left = None
                # 위로 옮기는 과정
                self.parent.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
            else : # 3-2. 삭제할 값이 부모 값보다 큰 경우 (오른쪽)
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left != None: # Change Node의 Left가 없을 때 까지 순회
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right != None: # Change Node의 Right 값이 있을 경우
                    self.change_node.parent.left = self.change_node.right # Change Node의 자식 노드를 Change Node(CN.P.l)랑 바꾼다.
                else : # 없는 경우
                    self.change_node_parent.left = None
                # 위로 옮기는 과정
                self.parent.right = self.change_node # parent 오른쪽을 change Node로 변경
                self.change_node.left = self.current_node.left # 연결
                self.change_node.right = self.current_node.right             


"""
랜덤 수 적용하기
"""
import random

bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print(bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = BST(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print ('search failed', num)


delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0,99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)