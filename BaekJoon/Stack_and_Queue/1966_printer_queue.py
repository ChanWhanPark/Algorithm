## 1966. 프린터 큐 (01.04)
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    importance_list = [0 for _ in range(n)]
    importance_list[m] = 1

    count = 0
    while True:
        if importance[0] == max(importance):
            count += 1

            if importance_list[0] != 1:
                del importance[0]
                del importance_list[0]
            else:
                print(count)
                break

        else:
            importance.append(importance[0])
            importance_list.append(importance_list[0])
            del importance[0]
            del importance_list[0]




