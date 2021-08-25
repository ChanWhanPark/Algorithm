## 볼링공 고르기
# 2019 SW 마에스트로 입학 테스트

n, m = map(int, input().split())
ball = list(map(int, input().split()))

count = 0
for i in range(len(ball)):
    for j in range(len(ball)):
        if i != j and ball[i] != ball[j]:
            count += 1


print(count//2)