def solution(price, money, count):
    pay = 0
    for i in range(1, count + 1):
        pay += (price * i)

    money -= pay
    if money >= 0:
        return 0
    else:
        return abs(money)

print(solution(3, 20, 4))
