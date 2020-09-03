## 2-2. 큰 수의 법칙 // 수식 이용

n, m, k = map(int, input().split()) ## n개의 자연수 입력, m번 연산, 하나의 수를 k번까지 반복
data = list(map(int, input().split()))

data.sort() # 입력받은 수 오름차수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

count = int(m / (k+1)) * k
count += (m % (k + 1)) # 가장 큰 수가 더해지는 횟수

result = 0
result += count * first # 가장 큰 수 더함
result += (m - count) * second # 두번째로 큰 수 더함

print(result)