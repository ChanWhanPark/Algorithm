# 문자열 재정렬 (08.26)
# Facebook 인터뷰

data = input()
result = []
num = 0
for d in data:
    if d.isalpha():
        result.append(d)
    else:
        num += int(d)

result.sort()

if num > 0:
    result.append(str(num))
print(''.join(result))
