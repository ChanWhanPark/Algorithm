## 자물쇠와 열쇠(08.27)
# 2020 카카오 신입 공채

def rotate_90(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j] # 시계 방향 90도 회전

    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    # 탐색 영역이 모두 1로 맞을 시에 열쇠가 맞는 것으로 반환
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False

    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 연산을 쉽게 하기 위해 자물쇠의 크기를 세배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 자물쇠 중앙에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]


    for rotation in range(4): # 네 방향 회전
        key = rotate_90(key)
        # 자물쇠 크기에서
        for x in range(n*2):
            for y in range(n*2):
                # 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:
                    return True

                # 열쇠를 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False





m, n = map(int, input().split())
key = []
lock = []

for i in range(m):
    key.append(list(map(int, input().split())))

for j in range(n):
    lock.append(list(map(int, input().split())))

print(solution(key, lock))