## 기둥과 보 설치(08.27)
# 2020 카카오 신입 공채


def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 기둥이면
            # 바닥 위 혹은 보의 한쪽 끝부분 위 혹은 다른 기둥 위라면 가능
            if y == 0 or [x-1,y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 설치된 것이 보라면
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])

        elif operate == 1: # 설치하는 경우
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)

a = [5, 5, 5]
b = [
        [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
        [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]],
        [[0,1,1,1],[5,0,0,1],[4,1,1,1]]
    ]
for x, y in zip(a, b):
    print(solution(x, y))