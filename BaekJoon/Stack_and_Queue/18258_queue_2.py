## 18258. 큐 2 (10.07)
import sys
from collections import deque
n = int(input())

queue = deque()
for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        queue.append(int(op[1]))
    elif op[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif op[0] == "size":
        print(len(queue))
    elif op[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif op[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])