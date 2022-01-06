## 5525. IOIOI (01.06)
n = int(input())
length = int(input())
string = input()

judge = "I"
for i in range(n):
    judge += "OI"

idx = 0
count = 0
while True:
    if string[idx:idx+len(judge)] == judge:
        count += 1
    idx += 1
    if idx == length - len(judge):
        break

print(count)
