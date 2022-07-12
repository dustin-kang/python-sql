class MaxHeap:
    def __init__(self, data):
        self.heap_array = list() # 배열 자료구조
        self.heap_array.append(None) # 인덱스 번호는 1번 부터 시작
        self.heap_array.append(data)
   
    def move_up(self, inserted_idx):
        """
        ### 데이터 SWAP에 대한 판단만 하는 함수
        - 자식 노드가 부모노드보다 데이터가 큰 경우 변경
        - 변경할 상황 이면 `True`
        - 변경할 필요 없으면 `False`
        """     
        if inserted_idx <= 1: # 데이터가 아예 없는 경우
            return False
        parent_idx = inserted_idx // 2 # 부모노드
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]: # 부모노드보다 큰 경우
            return True
        else : # 부모노드보다 작은 경우
            return False
        
    def insert(self, data):
        """
        ### 데이터 추가
        """
        if len(self.heap_array) == 0: # 예외 처리 (루트노드가 없는 경우)
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data) # 데이터 추가
        
        inserted_idx = len(self.heap_array) - 1 # 지금 추가된 노드의 인덱스 번호 
        
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2 # 부모노드
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] # swap
            inserted_idx = parent_idx # 인덱스 변경
            
        return True    
    
    def move_down(self, popped_idx):
        """
        ### 데이터 SWAP에 대한 판단만 하는 함수
        - 자식 노드가 부모노드보다 데이터가 큰 경우 변경
        - 변경할 상황이면 `True`
        - 변경할 필요 없으면 `False`
        """
        left_child_popped_idx = popped_idx * 2 # 삭제노드의 왼쪽 자식 노드
        right_child_popped_idx = popped_idx * 2 + 1 # 삭제노드의 오른쪽 자식 노드
        
        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array): 
            return False
        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # 부모노드보다 큰 경우
                return True
            else: # 부모 자식노드보다 작은 경우
                return False
        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]: # 왼쪽 자식노드가 오른쪽 자식노드보다 큰 경우
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # 2. 부모노드랑 비교
                    return True
                else:
                    return False
            else: # 오른쪽 자식노드가 왼쪽 자식노드보다 큰 경우
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:  # 부모노드랑 비교
                    return True
                else:
                    return False
                       
    
    
    def pop(self):
        """
        ### 데이터 삭제
        """
        if len(self.heap_array) <= 1: # 데이터가 아예 없는 경우
            return None
        
        returned_data = self.heap_array[1] # 루트 노드 데이터
        return returned_data

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
                
            
            if right_child_popped_idx >= len(self.heap_array): # Case 2 : 왼쪽 자식 노드만 있을 경우
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # 삭제할 노드 < 왼쪽 자식 노드
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx # Swap
                
            else :  # Case 3. 두 자식 노드 모두가 있을 때
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]: # 왼쪽 자식 > 오른쪽 자식
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # 왼쪽 자식 > 삭제할 노드
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx # Swap
                else: # 오른쪽 자식 > 오른쪽 자식
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]: # 오른쪽 자식 > 삭제할 노드
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx # Swap


heap = MaxHeap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.heap_array

heap.pop()

heap.heap_array