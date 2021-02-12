s = input() # 문자열 s
count_0 = 0 # 0으로 뒤집는 횟수
count_1 = 1 # 1로 뒤집는 횟수

# 첫번째 문자에 대한 처리
if s[0] == '1':
    count_0 += 1
elif s[0] == '0':
    count_1 += 1

# 두번째 문자부터에 대한 처리
for i in range(len(s) - 1):
    if s[i] != s[i-1]:
        # 다음 수에서 1로 바뀌는 경우
        if s[i] == '1':
            count_0 += 1
        elif s[i] == '0':
            count_1 += 1

print(min(count_0, count_1))