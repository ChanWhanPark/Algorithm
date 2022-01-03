## 2775. 부녀회장이 될테야 (01.03)
import sys
n = int(sys.stdin.readline())

for _ in range(n):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    apartment = [[0 for _ in range(room+1)] for _ in range(floor+1)]
    for i in range(floor+1):
        for j in range(1, room+1):
            if i == 0:
                apartment[i][j] = j
            else:
                if j == 1:
                    apartment[i][j] = 1
                else:
                    apartment[i][j] = sum(apartment[i-1][1:j+1])

    print(apartment[floor][room])