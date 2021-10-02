## 1018. 체스판 다시 칠하기 (10.02)
n, m = map(int, input().split())
chess_board = []
mini = []
for _ in range(n):
    chess_board.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0: # 짝수와 홀수일 때 각각 일정한 색을 가짐
                    if chess_board[k][l] != "W":
                        first_W += 1
                    if chess_board[k][l] != "B":
                        first_B += 1
                else:
                    if chess_board[k][l] != "B":
                        first_W += 1
                    if chess_board[k][l] != "W":
                        first_B += 1

        mini.append(first_W)
        mini.append(first_B)

print(min(mini))