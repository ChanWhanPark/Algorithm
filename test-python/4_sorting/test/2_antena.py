## 안테나 (08.30)
# 2019 SW 마에스트로 입학 테스트

n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(n-1) // 2])