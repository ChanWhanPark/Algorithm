n = input()
length = len(n)

result = 0
for i in range(length // 2):
    result += int(n[i])

for i in range(length // 2, length):
    result -= int(n[i])

if result == 0:
    print("LUCKY")
else:
    print("READY")