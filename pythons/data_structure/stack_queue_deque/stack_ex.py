stack = list()

def push(data):
    stack.append(data)

def pop():
    data = stack[-1]
    del stack[-1]
    return data

for index in range(10):
    push(index)

pop()