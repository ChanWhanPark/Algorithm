## 프로그래머스 위클리 챌린지 2주차 (09.01)

def grade(student_score, count):
    sum = 0
    for i in range(len(student_score)):
        if student_score[i] == -1:
            continue
        else:
            sum += student_score[i]

    avg = sum / count
    if avg >= 90:
        grades = "A"
    elif avg >= 80 and avg < 90:
        grades = "B"
    elif avg >= 70 and avg < 80:
        grades = "C"
    elif avg >= 50 and avg < 70:
        grades = "D"
    else:
        grades = "F"

    return grades

def solution(scores):
    answer = ""
    length = len(scores)
    max_score = -1e9
    min_score = 1e9
    max_index = -1
    min_index = -1
    student_score = []
    count = 0
    for i in range(length):
        for j in range(length):
            student_score.append(int(scores[j][i]))
            temp = scores[j][i]
            if temp >= max_score:
                max_score = temp
                max_index = j
            elif temp < min_score:
                min_score = temp
                min_index = j

        current_index = i

        if current_index == max_index or current_index == min_index:
            student_score[current_index] = -1

        for k in range(len(student_score)):
            if student_score[k] != -1:
                count += 1

        student_grade = grade(student_score, count)
        answer += student_grade
        max_index, min_index = -1, -1
        max_score = -1e9
        min_score = 1e9
        count = 0
        student_score = []

    return answer

scores = [
    [100, 90, 98, 88, 65],
    [50, 45, 99, 85, 77],
    [47, 88, 95, 80, 67],
    [61, 57, 100, 80, 65],
    [24, 90, 94, 75, 65]
]
print(solution(scores))