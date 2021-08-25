# 문자열 뒤집기(08.25)

data = input()
zero_count = 0
one_count = 0

# 첫번째 데이터에 대해
if data[0] == '0':
    zero_count += 1
elif data[0] == '1':
    one_count += 1

# 두번째 이후의 데이터에 대해
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '0':
            zero_count += 1
        elif data[i+1] == '1':
            one_count += 1


print(min(zero_count, one_count))