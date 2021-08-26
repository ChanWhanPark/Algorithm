## 럭키 스트레이트(08.26)

data = input()
left_num = 0
right_num = 0
for i in range(len(data)//2):
    left_num += int(data[i])

for j in range(len(data)-1, (len(data) // 2)-1, -1):
    right_num += int(data[j])

if left_num == right_num:
    print("LUCKY")
else:
    print("READY")