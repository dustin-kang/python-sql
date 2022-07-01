queue = list()

def enqueue(data):
    queue.append(data)


def dequeue():
    data = queue[0]
    del queue[0]
    return data

for i in range(len(1,10)):
    enqueue(i)

dequeue()