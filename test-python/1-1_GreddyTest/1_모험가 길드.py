n = int(input()) # 모험가 수 N 입력
data = list(map(int, input().split())) # 공포도 입력
data.sort() # 데이터 오름차순으로 정렬

group = 0 # 그룹의 수
count = 0 # 그룹에 포함된 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 모험가 포함
    if count >= i: # 모험가 수가 공포도 이상이라면
        group += 1 # 그룹 수 증가
        count = 0 # 모험가 수 초기화

print(group)

# 공포도 1인 사람은 1명, 2인 사람은 2명, 3인 사람은 3명, ..., N인 사람은 N명끼리 그룹을 지으며
# 그룹이 이뤄지지 않으면 마을에 남아도 되기 때문에, 모든 모험가를 특정한 그룹에 넣지 않아도 됨.