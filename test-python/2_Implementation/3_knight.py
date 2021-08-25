## 왕실의 나이트(08.25)

input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - 96

count = 0

steps = [
    (2, -1), (2, 1), (1, -2), (1, 2),
    (-1, -2), (-1, 2), (-2, -1), (-2, 1)
]

for s in steps:
    next_row = row + s[1]
    next_column = row + s[0]

    if next_row > 8 or next_row < 1 or next_column > 8 or next_column < 1:
        continue
    else:
        count += 1

print(count)