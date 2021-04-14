from collections import deque

queue=[10,40,30]
queue=deque(queue)

queue.append(50)
print(queue)

queue.append(80)
print(queue)

queue.append(90)
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)