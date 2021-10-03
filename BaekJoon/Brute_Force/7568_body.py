## 7568. 덩치 (10.03)

n = int(input())
body = []
grade_list = []
for _ in range(n):
    x, y = map(int, input().split())
    body.append([x, y])

for i in range(n):
    grade = 1
    for j in range(n):
        if i != j:
            if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
                grade += 1

    grade_list.append(grade)
    print(grade_list[i], end = ' ')