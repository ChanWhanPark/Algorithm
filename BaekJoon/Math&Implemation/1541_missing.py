## 1541. 잃어버린 괄호 (01.05)
formular = input().split('-')
ans = 0
for i in formular[0].split('+'):
    ans += int(i)
for i in formular[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)
