## 18111. 마인크래프트 (01.05)

n, w, b = map(int, input().split())
space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

min_value = min(map(min, space))
max_value = max(map(max, space))
leastTime = 1e9

for i in range(min_value, max_value+1):
    pluscount = 0
    minuscount = 0
    for j in range(n):
        for k in range(w):
            h = space[j][k] - i
            if h > 0:
                minuscount += h
            elif h < 0:
                pluscount -= h

    if minuscount + b >= pluscount:
        time = minuscount * 2 + pluscount
        if leastTime >= time:
            leastTime = time
            resultHeight = i

print(leastTime, resultHeight)