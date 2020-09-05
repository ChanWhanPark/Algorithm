# 1-5. 입력한 수 이하의 소수 나열하기

counter = 0

num = int(input("정수 입력: "))
for i in range(2, num):
    for j in range(2, i):
        counter += 1
        if i % j == 0: # 나눠떨어지면 소수가 아님
            break
    else:
        print(i)

print(f'나눗셈을 실행한 횟수: {counter}')