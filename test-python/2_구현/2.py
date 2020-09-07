# 현재 나이트의 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트의 이동 가능 범위
step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for s in step:
    next_row = row + s[0]
    next_column = column + s[1]

    if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)