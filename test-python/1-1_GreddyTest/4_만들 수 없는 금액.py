# 동전의 개수 입력
n = int(input())
# 화폐 단위 입력
money = list(map(int, input().split()))
money.sort()

target = 1
for x in money:
    # 만들 수 없는 금액을 찾았을 때 종료
    if target < x:
        break
    else:
        target += 1

print(target)