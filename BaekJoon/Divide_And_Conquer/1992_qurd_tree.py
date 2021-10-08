## 1992. 쿼드트리 (10.08)
def press(x, y, len):
    check = num_list[x][y]
    for i in range(x, x+len):
        for j in range(y, y+len):
            if check != num_list[i][j]:
                print("(", end="")
                press(x, y, len//2)
                press(x, y+len//2, len//2)
                press(x+len//2, y, len//2)
                press(x+len//2, y+len//2, len//2)
                print(")", end="")
                return

    print(check, end="")



n = int(input())
num_list = [list(map(int, input())) for _ in range(n)]
press(0, 0, n)