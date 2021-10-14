## 11723. 집합 (10.12)
import sys
n = int(input())

S = []

for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "add":
        if int(op[1]) in S:
            pass
        else:
            S.append(int(op[1]))
    elif op[0] == "remove":
        if int(op[1]) not in S:
            pass
        else:
            S.remove(int(op[1]))
    elif op[0] == "check":
        if int(op[1]) in S:
            print(1)
        else:
            print(0)
    elif op[0] == "toggle":
        if int(op[1]) in S:
            S.remove(int(op[1]))
        else:
            S.append(int(op[1]))
    elif op[0] == "all":
        S = [i for i in range(1, 21)]
    elif op[0] == "empty":
        S = []

    S = sorted(S)


