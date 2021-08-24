## 거스름돈 구하기(08.24)

money = int(input())
coin = [500, 100, 50, 10]
money_count = 0

for c in coin:
    money_count += (money // c)
    money %= c

print(money_count)