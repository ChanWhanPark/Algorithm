## 1. 그리디 기본

money = int(input("금액 입력: "))
coin = [500, 100, 50, 10]
count = 0
for i in coin:
    count += money // i  # //는 정수만 나오는 나눗셈 연산
    money %= i

print(count)