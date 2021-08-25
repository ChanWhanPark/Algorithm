# 모험가 길드(08.25)

n = int(input())
character = list(map(int, input().split()))
group = 0
count = 0

character.sort()

for c in character: # 공포감 느끼는 캐릭터 순
    count += 1 # 공포감 느끼는 인원 하나
    if count >= c: # 인원이 공포감보다 크거나 같을 경우
        group += 1 # 그룹을 하나 채우고
        count = 0 # 다음 그룹으로 이동

print(group)