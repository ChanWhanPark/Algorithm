## 1780. 종이의 개수 (10.08)
def cut(x, y, n):
    global zero, plus, minus
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        cut(x + k * n//3, y + l * n//3, n//3)
                return
    if check == -1:
        minus += 1
        return
    elif check == 0:
        zero += 1
        return
    else:
        plus += 1
        return

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

zero = 0
plus = 0
minus = 0

cut(0, 0, n)
print(minus)
print(zero)
print(plus)