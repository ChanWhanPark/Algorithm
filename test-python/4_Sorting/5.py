n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# 키 이용, 점수 기준 정렬
array = sorted(array, key=lambda student: student[1], reverse = True)

for student in array:
    print(student[0], end=' ')