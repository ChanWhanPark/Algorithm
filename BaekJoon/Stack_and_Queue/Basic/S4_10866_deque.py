## 10868. 덱 (10.02) S4
import sys
n = int(input())
deque = []
for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "push_front":
        deque.insert(0, op[1])
    elif op[0] == "push_back":
        deque.insert(len(deque), op[1])
    elif op[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif op[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif op[0] == "size":
        print(len(deque))
    elif op[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif op[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
