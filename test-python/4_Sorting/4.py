n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True) # 내림차순

print(array)