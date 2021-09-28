## 5185. 이진수 (09.28)
T = int(input())
answer = []
def change_decimal(num):
    binary = ""
    for _ in range(4):
        left = num % 2
        binary += str(left)
        num //= 2
    if len(binary) != 4:
        for _ in range(4-len(binary)+1):
            binary += '0'

    return binary[::-1]

for test_case in range(1, T + 1):
    n, hex_num = input().split()
    result = ""
    for i in range(int(n)):
        if hex_num[i] >= '0' and hex_num[i] <= '9':
            h = int(hex_num[i])
            bin = change_decimal(h)
        else:
            h = ord(hex_num[i]) - 55
            bin = change_decimal(h)
        result += bin

    answer.append(result)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))