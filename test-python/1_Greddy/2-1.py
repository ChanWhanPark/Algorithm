## 2-1. 큰 수의 법칙 // while문 이용

n, m, k = map(int, input().split()) ## n개의 자연수 입력, m번 연산, 하나의 수를 k번까지 반복
data = list(map(int, input().split()))

data.sort() # 입력받은 수 오름차수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0
while True: # 무한루프
    for i in range(k):
        if m == 0: break; # m = 0이면 for문 종료
        result += first
        m -= 1 # 더할 때마다 1씩 감소
    if m == 0: break;
    result += second
    m -= 1;

print(result)