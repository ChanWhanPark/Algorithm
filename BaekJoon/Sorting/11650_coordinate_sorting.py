## 11650. 좌표 정렬하기 (10.05)
## 11651. 좌표 정렬하기 2 (10.05)
n = int(input())
coord = []
for _ in range(n):
    a, b = map(int, input().split())
    coord.append([a, b])

coord = sorted(coord, key=lambda x:(x[0], x[1]))
#coord = sorted(coord, key=lambda x:(x[1], x[0]))
for x, y in coord:
    print(x, y)