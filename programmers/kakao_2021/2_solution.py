import math

def change_dimension(n, k):
    new_number = ""
    while True:
        if n == 0:
            break
        else:
            new_number += str(n % k)
            n //= k
    return new_number[::-1]

def split_zero(lst):
    new_lst = []
    append_str = ''
    for i in range(len(lst)):
        if lst[i] == '0':
            new_lst.append(append_str)
            append_str = ''
        else:
            append_str += lst[i]
    print(new_lst)
    for _ in range(10):
        for e in new_lst:
            if e == '':
                new_lst.remove(e)
    return new_lst

def prime_check(number_list):
    result = 0
    check = True
    for num in number_list:
        if num != 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    check = False
            if check == True:
                result += 1
    return result

def solution(n, k):
    num_list = change_dimension(n, k)
    print(num_list)
    new_list = split_zero(num_list)
    print(new_list)
    new_list_num = list(map(int, new_list))
    answer = prime_check(new_list_num)
    return answer

print(solution(100000000, 10))