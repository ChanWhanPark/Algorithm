## 문자열 압축(08.26)
# 2020 카카오 신입 공채

def compress(string):
    answer = len(string)
    count = 1
    # 압축 단위를 하나씩 늘려가면서 확인
    for step in range(1, len(string) // 2 + 1):
        compressed = ""
        prev = string[0:step]
        for j in range(step, len(string), step):
            # 이전 상태와 동일하면 압축 횟수 증가
            if prev == string[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = string[j:j+step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))


    return answer

data = input()
print(compress(data))