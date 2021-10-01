## 2798. 블랙잭 (10.01)
from itertools import permutations

n, m = map(int, input().split())
card = list(map(int, input().split()))
card_list_for_three = permutations(card, 3)
card_sum = []

for c in card_list_for_three:
    card_sum.append(sum(c))

card_sum.sort()
for s in range(len(card_sum)):
    if card_sum[s] == m:
        print(m)
        break
    if card_sum[s] > m:
        print(card_sum[s-1])
        break
    if s == len(card_sum) - 1:
        print(card_sum[s])
