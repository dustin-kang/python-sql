class Stack:
  """
  - self.data : 동적 처리로 대괄호만 선언하여 값을 정해놓지 않는다.
  - push : 인덱스 추가
  - pop : 인덱스의 마지막 노드 추출
  """
  def __init__(self):
    self.data = [] 

  def push(self, item):
    self.data.append(item)

  def pop(self): # 삭제하는게 아니라 추출한다의 개념
    if len(self.data) > 0 : # 언더 플로우 방지
        return self.data.pop()
    return "스택이 비었습니다."