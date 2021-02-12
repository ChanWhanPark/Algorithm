s = input() # 숫자로 된 문자열 만들기

n = int(s[0]) # 첫번째 숫자
for i in range(1, len(s)):
    num = int(s[i]) # i-1번째 숫자
    if n <= 1 or num <= 1: # 첫번째 수가 0 또는 1이거나 다음 수가 0이나 1이면 더하기를 선택
        n += num 
    else: # 이외에는 곱하기를 선택
        n *= num

print(n)


