# 만들 수 없는 금액(08.25)
# K 대회 기출

n = int(input())
money = list(map(int, input().split()))
money.sort()

target = 1
for m in money:
    if target < m:
        break
    target += m

print(target)