## 튜플 (10.09)
def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key=len)

    answer = []
    for i in s:
        ii = i.split(",")
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))

    return answer


s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s1))

s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s2))