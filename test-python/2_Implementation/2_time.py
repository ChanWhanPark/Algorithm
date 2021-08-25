## 시각(3이 포함되면 모조리 세는 경우) (08.25)
hour = int(input())

count = 0

for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)