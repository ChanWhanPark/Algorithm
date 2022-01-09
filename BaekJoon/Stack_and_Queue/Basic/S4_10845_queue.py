## 10845. 큐 (10.02 01.09) S4
import sys

n = int(input())
queue = []
for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        queue.append(op[1])
    elif op[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
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
