## 10828. 스택 (10.02)
import sys

n = int(input())
stack = []
for i in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        stack.append(op[1])
    elif op[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif op[0] == "size":
        print(len(stack))
    elif op[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])

