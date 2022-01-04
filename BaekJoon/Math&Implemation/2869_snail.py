# 2869. 달팽이는 올라가고 싶다 (01.03)

a, b, v = map(int, input().split())
day = (v - b) / (a - b) # 이항 정리로 도출
# (a * day) - b * (day - 1) >= v

print(int(day) if day == int(day) else int(day) + 1)