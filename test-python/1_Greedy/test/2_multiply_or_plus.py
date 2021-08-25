## 곱하기 혹은 더하기(08.25)
## Facebook 인터뷰

number = input()
result = int(number[0])

for n in range(1, len(number)):
    num = int(number[n])
    if num <= 1 or result == 0:
        result += num
    else:
        result *= num

print(result)