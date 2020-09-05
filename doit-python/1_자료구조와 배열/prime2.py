#1-6. 입력한 수 이하의 소수 나열하기(알고리즘 개선 1)

counter = 0
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수 저장 배열

prime[ptr] = 2 # 초깃값
ptr += 1

num = int(input("정수 입력: "))
for n in range(3, num, 2): # 홀수만 대상, 짝수는 2로 나눠떨어짐
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0: # 나누어 떨어지면 소수가 아님
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')