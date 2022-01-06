## 18870. 좌표 압축 (01.06)
n = int(input())
coor_list = list(map(int, input().split()))

coor_list2 = sorted(list(set(coor_list)))
dic = {coor_list2[i] : i for i in range(len(coor_list2))}

print(coor_list, coor_list2, dic)
for i in coor_list:
    print(dic[i], end = " ")