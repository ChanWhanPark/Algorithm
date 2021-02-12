string = input()
string_list = []
num = 0

for i in string:
    if i.isalpha():
        string_list.append(i)
    else:
        num += int(i)

string_list.sort()

if num != 0:
    string_list.append(str(num))

print(''.join(string_list))