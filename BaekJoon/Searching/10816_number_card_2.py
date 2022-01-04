## 10816. 숫자 카드 2 (01.04)
from collections import Counter
n = int(input())
card = list(map(int, input().split()))
card_count = Counter(card).most_common()
card_count.sort()

m = int(input())
find = list(map(int, input().split()))
answer = []

for f in find:
    flag = 0
    for c in card_count:
        if f == c[0]:
            answer.append(c[1])
            flag = 1
    if flag == 0:
        answer.append(0)

for a in answer:
    print(a, end = " ")