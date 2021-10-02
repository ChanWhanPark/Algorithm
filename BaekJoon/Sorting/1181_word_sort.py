## 1181. 단어 정렬 (10.02)
n = int(input())
word_list = []

for i in range(n):
    word = input()
    word_list.append([len(word), word])

new_word_list = sorted(word_list, key=lambda x:(x[0], x[1]))

print(new_word_list[0][1])
for i in range(1, len(new_word_list)):
    if new_word_list[i-1] == new_word_list[i]:
        continue
    else:
        print(new_word_list[i][1])


