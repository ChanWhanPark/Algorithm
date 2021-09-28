## 4831 전기 버스(09.07)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    charger = list(map(int, input().split()))
    charge = [0] * (n+1)
    visited = [0] * (n+1)
    for i in charger:
        charge[i] = 1

    distance = k
    current = k
    while True:
        if current >= n:
            result = sum(visited)
            break

        if charge[current] == 1: # 충전기가 있는 곳일 때
            distance = k # 최대 이동가능 거리로 변경
            visited[current] = 1 # 방문 처리
            current += k # 현 위치도 그만큼 이동

        elif charge[current] == 0: # 충전기가 없는 곳일 때
            distance -= 1 # 최대 이동 가능거리에서 1 빼기
            current -= 1 # 현 위치 뒤로 이동
            if distance == 0: # 정류장이 범위 내에 없을 경우
                result = 0 # 불가능
                break

    answer.append(result)




for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))