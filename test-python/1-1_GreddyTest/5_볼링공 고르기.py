n, m = map(int, input().split()) # 볼링공 개수 n, 공의 무게 m
k = list(map(int, input().split())) # 각 볼링공의 무게 k

weight = [0] * 11 # 무게는 0부터 10까지 담을 수 있음
for x in k:
    weight[x] += 1 # 각 볼링공의 무게가 존재할 때마다 개수를 1씩 늘림

case = 0

for i in range(1, m+1): # 1부터 최고 무게까지 처리
    n -= weight[i] # 무게가 i인 볼링공의 개수 제외
    case += array[i] * n # B가 선택하는 경우의 수만큼 곱함

print(case) 