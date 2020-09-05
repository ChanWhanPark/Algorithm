#1-7. 입력한 수 이하의 소수 나열하기(알고리즘 개선 2)

counter = 0
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수 저장 배열

prime[ptr] = 2 # 초깃값
ptr += 1

prime[ptr] = 3
ptr += 1

num = int(input("정수 입력: "))
for n in range(5, num, 2): # 홀수만을 대상으로 함
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break;
        i += 1
    else:
        prime[ptr] = n # 소수이므로 배열에 등록
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print(f'연산 횟수 : {counter}')