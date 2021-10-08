## 5430. AC (10.08)
import sys

T = int(input())
for _ in range(T):
    op = sys.stdin.readline().rstrip()
    n = int(input())
    arr = input()[1:-1].split(',')

    op = op.replace("RR", "")

    error_flag = 0

    for o in op:
        if o == "R":
            arr.reverse()
        elif o == "D":
            if len(arr) == 0 or arr[0] == '':
                error_flag = 1
                break
            else:
                arr.pop(0)

    if error_flag == 1:
        print("error")
    else:
        print("[", end = "")
        for i in range(len(arr)-1):
            print("%d," % (int(arr[i])), end="")
        if len(arr) != 0:
            print("%d]" % (int(arr[len(arr)-1])))
        else:
            print("]")