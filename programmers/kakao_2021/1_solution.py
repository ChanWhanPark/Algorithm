def check_same(report_list, i):
    for j in range(len(report_list)):
        if report_list[i] == report_list[j] and i != j:
            return True
    return False

def solution(id_list, report, k):
    report_list = []  # 신고한 사람과 신고당한 사람의 쌍
    for r in report:
        report_list.append([r[0:int(r.index(" "))], r[int(r.index(" ")) + 1:len(r)]])
        # 신고한 사람과 신고당한 사람 분리

    print(report_list)
    reported_count = [0] * len(id_list)
    report_count = [0] * len(id_list)
    stopped_check = [0] * len(id_list)
    visited_check = [0] * len(id_list)

    for i in range(len(report_list)):
        if report_list[i][1] in id_list:
            if check_same(report_list, i):
                continue
            else:
                reported_count[int(id_list.index(report_list[i][1]))] += 1  # 신고당한 횟수 카운트
                print(i+1)
                if reported_count[int(id_list.index(report_list[i][1]))] >= k and stopped_check[int(id_list.index(report_list[i][1]))] == 0: # 정지 대상이 된다면,
                    stopped_check[int(id_list.index(report_list[i][1]))] = 1 # 그 유저를 정지 대상으로 변환
                    for j in range(i):
                        if [report_list[j][0], report_list[i][1]] in report_list and visited_check[j] == 0:
                            report_count[int(id_list.index(report_list[j][0]))] += 1
                            visited_check[j] = 1
                            print(report_list[j][0], report_list[i][1])



    print(id_list)
    print(reported_count)
    print(stopped_check)
    print(report_count)



    return

id_list = 	["a", "b", "c", "d"]
report =  ["a c","a d","b a","b d","d a"]
k = 2

solution(id_list, report, k)