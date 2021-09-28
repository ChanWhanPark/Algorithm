## 5186. 이진수 2 (09.28)
T = int(input())
answer = []
def change_decimal(num):
    new_num = float(num)
    bin = ""
    length = 0
    while length <= 12:
        new_num *= 2
        if new_num >= 1:
            bin += "1"
            new_num -= 1
        else:
            bin += "0"
        length += 1
        if new_num == 0:
            return bin

    return "overflow"

for test_case in range(1, T + 1):
    minor_num = input()
    result = change_decimal(minor_num)

    answer.append(result)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))