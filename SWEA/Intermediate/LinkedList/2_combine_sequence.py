## 5110. 수열 합치기 (09.16)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    linked_list = list(map(int, input().split()))
    for _ in range(m-1):
        lst = list(map(int, input().split()))
        check = True
        for i in range(len(linked_list)):
            if linked_list[i] > lst[0]: # 삽입할 원소보다 크면
                linked_list[i:i] = lst
                check = False
                break

        if check: # 찾지 못하면 끝부분에 추가
            linked_list.extend(lst)

    sorted_link = linked_list[len(linked_list)-10:]
    sorted_link.reverse()

    answer.append(' '.join(map(str, sorted_link)))

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))