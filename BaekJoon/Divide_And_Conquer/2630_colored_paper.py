## 2630. 색종이 만들기(10.07)
def cut(x, y, n):
    global white, blue
    check = paper_list[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper_list[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

n = int(input())
paper_list = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

cut(0, 0, n)
print(white)
print(blue)
