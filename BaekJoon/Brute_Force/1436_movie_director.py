## 1436. 영화감독 숌 (10.03)
n = int(input())
number = 0
count = 0

while True:
    number += 1
    num_list = str(number)
    if number >= 100:
        for i in range(len(str(number))):
            if num_list[i:i+3] == '666':
                count += 1
                break

    if count == n:
        print(number)
        break
